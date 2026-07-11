document.addEventListener('DOMContentLoaded', () => {
  AOS.init({duration: 700, once: true});
  const text = 'Premium drops, seamless checkout, authentic comfort.';
  const typing = document.querySelector('.typing-text');
  if (typing) {
    let i = 0;
    const type = () => {
      typing.textContent = text.slice(0, i);
      i++;
      if (i <= text.length) setTimeout(type, 50);
    };
    type();
  }
  const backToTop = document.getElementById('backToTop');
  if (backToTop) {
    window.addEventListener('scroll', () => backToTop.style.display = window.scrollY > 600 ? 'block' : 'none');
    backToTop.addEventListener('click', () => window.scrollTo({top:0,behavior:'smooth'}));
  }
  const countdown = document.querySelector('.countdown');
  if (countdown) {
    const deadline = new Date(countdown.dataset.deadline);
    const tick = () => {
      const diff = deadline - new Date();
      if (diff <= 0) { countdown.innerHTML = '<div class="fw-bold">Sale ended</div>'; return; }
      const days = Math.floor(diff / (1000 * 60 * 60 * 24));
      const hours = Math.floor((diff / (1000 * 60 * 60)) % 24);
      const mins = Math.floor((diff / (1000 * 60)) % 60);
      const secs = Math.floor((diff / 1000) % 60);
      countdown.innerHTML = `<div class="d-flex gap-3 flex-wrap"><div class="glass-card px-3 py-2"><strong>${days}</strong><div class="small text-muted">Days</div></div><div class="glass-card px-3 py-2"><strong>${hours}</strong><div class="small text-muted">Hours</div></div><div class="glass-card px-3 py-2"><strong>${mins}</strong><div class="small text-muted">Mins</div></div><div class="glass-card px-3 py-2"><strong>${secs}</strong><div class="small text-muted">Secs</div></div></div>`;
    };
    tick();
    setInterval(tick, 1000);
  }
});
