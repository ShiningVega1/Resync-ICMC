const menu = document.querySelector('.menu');
const nav = document.querySelector('nav');

if (menu && nav) {
  menu.addEventListener('click', () => {
    const open = menu.getAttribute('aria-expanded') !== 'true';
    menu.setAttribute('aria-expanded', String(open));
    nav.classList.toggle('open', open);
  });

  nav.addEventListener('click', (e) => {
    if (e.target.closest('a')) {
      menu.setAttribute('aria-expanded', 'false');
      nav.classList.remove('open');
    }
  });

  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && nav.classList.contains('open')) {
      nav.classList.remove('open');
      menu.setAttribute('aria-expanded', 'false');
      menu.focus();
    }
  });

  window.addEventListener('resize', () => {
    if (window.innerWidth > 760) {
      nav.classList.remove('open');
      menu.setAttribute('aria-expanded', 'false');
    }
  });

  const path = location.pathname.split('/').pop() || 'index.html';
  nav.querySelectorAll('a').forEach((a) => {
    const href = (a.getAttribute('href') || '').split('#')[0];
    if (href === path) a.setAttribute('aria-current', 'page');
  });
}

document.querySelectorAll('form.demo-form').forEach((form) => {
  form.addEventListener('submit', (e) => {
    e.preventDefault();
    if (!form.reportValidity()) return;

    const fields = [...form.querySelectorAll('[required]')];
    const empty = fields.find((f) => !f.value.trim());
    if (empty) {
      empty.setCustomValidity('Please complete this field.');
      empty.reportValidity();
      return;
    }

    const status = form.querySelector('[role=status]');
    if (status) {
      status.textContent = 'Validation passed. This is a prototype: your message has not been sent or stored. Please use the email or phone number shown to contact ICMC.';
      status.focus();
    }
  });

  form.querySelectorAll('input,textarea').forEach((f) => f.addEventListener('input', () => f.setCustomValidity('')));
});

// CMS-powered community content; generated during GitHub Pages deployment.
(() => {
  const outputs = [...document.querySelectorAll('[data-content-list]')];
  const carousel = document.querySelector('[data-announcement-carousel]');
  if (!outputs.length && !carousel) return;
  const esc = s => String(s ?? '').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
  const today = new Date().toISOString().slice(0,10);
  const active = item => item.published === true && (!item.expires || item.expires >= today);
  const safeLink = url => {
    if (!url) return '';
    try { const u=new URL(url,location.href); return ['http:','https:'].includes(u.protocol)?u.href:''; }
    catch {return '';}
  };
  const card = (item,kind) => {
    const url=safeLink(item.link);
    return '<article class="cms-entry"><p class="cms-date">'+esc(item.date)+'</p><h3>'+esc(item.title)+'</h3><p>'+esc(item.summary)+'</p>'+(item.body?'<p>'+esc(item.body)+'</p>':'')+(url?'<a href="'+esc(url)+'" rel="noopener noreferrer">More information ↗</a>':'')+'</article>';
  };
  fetch('content/feed.json',{cache:'no-cache'}).then(r=>{if(!r.ok)throw Error('Feed unavailable');return r.json();}).then(feed=>{
    outputs.forEach(out=>{
      const kind=out.dataset.contentList;
      const entries=(feed[kind]||[]).filter(active).sort((a,b)=>kind==='events'?a.date.localeCompare(b.date):b.date.localeCompare(a.date));
      out.innerHTML=entries.length?entries.map(x=>card(x,kind)).join(''):'<p>No published updates at this time.</p>';
    });
    if(carousel){
      const slides=(feed.announcements||[]).filter(x=>active(x)&&x.featured).sort((a,b)=>{const x=Number.isFinite(Number(a.order))&&a.order!==''&&a.order!=null?Number(a.order):9999;const y=Number.isFinite(Number(b.order))&&b.order!==''&&b.order!=null?Number(b.order):9999;return x-y || b.date.localeCompare(a.date);});
      if(!slides.length){carousel.innerHTML='<p>No featured announcements at this time. <a href="announcements.html">View announcements</a>.</p>';return;}
      let index=0,timer;
      carousel.innerHTML='<div class="cms-slide" aria-live="polite"></div><div class="cms-controls"><button type="button" data-prev aria-label="Previous announcement">‹</button><span class="cms-count"></span><button type="button" data-next aria-label="Next announcement">›</button></div>';
      const draw=()=>{const x=slides[index],link=safeLink(x.link),slide=carousel.querySelector('.cms-slide');
        slide.innerHTML='<p class="cms-date">'+esc(x.date)+'</p><h3>'+esc(x.title)+'</h3><p>'+esc(x.summary)+'</p>'+(link?'<a href="'+esc(link)+'" rel="noopener noreferrer">Read more ↗</a>':'<a href="announcements.html">All announcements →</a>');
        carousel.querySelector('.cms-count').textContent=(index+1)+' / '+slides.length;
      };
      const move=n=>{index=(index+n+slides.length)%slides.length;draw();};
      const start=()=>{clearInterval(timer);if(slides.length>1&&!matchMedia('(prefers-reduced-motion: reduce)').matches)timer=setInterval(()=>move(1),7000);};
      carousel.querySelector('[data-prev]').onclick=()=>{move(-1);start();};
      carousel.querySelector('[data-next]').onclick=()=>{move(1);start();};
      carousel.addEventListener('mouseenter',()=>clearInterval(timer));
      carousel.addEventListener('mouseleave',start);
      carousel.addEventListener('focusin',()=>clearInterval(timer));
      carousel.addEventListener('focusout',start);
      draw();start();
    }
  }).catch(()=>{outputs.forEach(out=>out.innerHTML='<p>Updates are temporarily unavailable.</p>');if(carousel)carousel.innerHTML='<p>Announcements are temporarily unavailable. <a href="announcements.html">View updates</a>.</p>';});
})();
