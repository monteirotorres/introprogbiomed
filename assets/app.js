/* ============================================================
   Runtime: navegação por tópicos (SPA), tema, sidebar mobile
   Inspirado no curso de Bioestatística (IBCCF/UFRJ)
   ============================================================ */

function showTopic(target) {
  document.querySelectorAll('.topic').forEach(t =>
    t.classList.toggle('active', t.id === target));
  document.querySelectorAll('.nav-link').forEach(a =>
    a.classList.toggle('active', a.dataset.target === target));
  // re-highlight Prism dentro do tópico ativo
  if (window.Prism) Prism.highlightAll();
}

window.addEventListener('DOMContentLoaded', () => {
  // navegação por links da sidebar (mesma página)
  document.querySelectorAll('.nav-link[data-target]').forEach(a => {
    a.addEventListener('click', e => {
      e.preventDefault();
      const target = a.dataset.target;
      showTopic(target);
      history.replaceState(null, '', '#' + target);
      window.scrollTo({ top: 0, behavior: 'smooth' });
      document.querySelector('.sidebar')?.classList.remove('open');
    });
  });

  // ativa pelo hash, senão o primeiro tópico
  const hash = decodeURIComponent(window.location.hash.slice(1));
  if (hash && document.getElementById(hash)) showTopic(hash);
  else { const first = document.querySelector('.topic'); if (first) showTopic(first.id); }

  // responde a mudanças de hash (ex.: clique vindo de outra página)
  window.addEventListener('hashchange', () => {
    const h = decodeURIComponent(window.location.hash.slice(1));
    if (h && document.getElementById(h)) showTopic(h);
  });

  // toggle sidebar mobile
  document.getElementById('menuToggle')?.addEventListener('click', () => {
    document.querySelector('.sidebar')?.classList.toggle('open');
  });

  // colapsar/expandir grupos da sidebar
  document.querySelectorAll('.nav-group-title').forEach(t => {
    t.addEventListener('click', () => t.parentElement.classList.toggle('collapsed'));
  });

  // alternar tema claro/escuro
  document.getElementById('themeToggle')?.addEventListener('click', () => {
    const dark = document.documentElement.getAttribute('data-theme') === 'dark';
    if (dark) document.documentElement.removeAttribute('data-theme');
    else document.documentElement.setAttribute('data-theme', 'dark');
    try { localStorage.setItem('tema', dark ? 'light' : 'dark'); } catch (e) {}
  });
});
