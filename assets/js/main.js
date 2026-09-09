/* ==========================================================================
   TBWI — home page behaviour.

   Progressive enhancement throughout. index.html carries a `no-js` class that
   this script removes; the CSS uses `.no-js` to fall back to plain stacked
   layouts for the two scroll-driven sections. Anyone who prefers reduced
   motion, or is under 900px, gets those same fallbacks, applied here as
   .services--static / .process--static.
   ========================================================================== */

(function () {
  'use strict';

  document.documentElement.classList.remove('no-js');

  var reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
  var narrow = window.matchMedia('(max-width: 900px)');

  function prefersStatic() { return reduceMotion.matches || narrow.matches; }

  // One rAF-throttled scroll pass drives everything below.
  var handlers = [];
  var ticking = false;
  function onScroll() {
    if (ticking) return;
    ticking = true;
    requestAnimationFrame(function () {
      ticking = false;
      for (var i = 0; i < handlers.length; i++) handlers[i]();
    });
  }
  window.addEventListener('scroll', onScroll, { passive: true });

  /* --- Header ---------------------------------------------------------- */

  var header = document.querySelector('.site-header');
  if (header) {
    handlers.push(function () {
      header.classList.toggle('is-stuck', window.scrollY > 40);
    });
  }

  /* --- Mobile nav ------------------------------------------------------ */

  var toggle = document.querySelector('.nav-toggle');
  var mobileNav = document.querySelector('.mobile-nav');
  if (toggle && mobileNav) {
    var setNav = function (open) {
      toggle.setAttribute('aria-expanded', String(open));
      mobileNav.hidden = !open;
      document.body.classList.toggle('nav-open', open);
    };
    toggle.addEventListener('click', function () {
      setNav(toggle.getAttribute('aria-expanded') !== 'true');
    });
    mobileNav.addEventListener('click', function (e) {
      if (e.target.closest('a')) setNav(false);
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && toggle.getAttribute('aria-expanded') === 'true') {
        setNav(false);
        toggle.focus();
      }
    });
  }

  /* --- Scroll reveal ---------------------------------------------------- */

  var revealables = document.querySelectorAll('.reveal');
  if (revealables.length && 'IntersectionObserver' in window) {
    var revealObserver = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        entry.target.classList.add('is-visible');
        revealObserver.unobserve(entry.target);
      });
    }, { rootMargin: '0px 0px -10% 0px', threshold: 0.08 });
    revealables.forEach(function (el) { revealObserver.observe(el); });
  } else {
    revealables.forEach(function (el) { el.classList.add('is-visible'); });
  }

  /* --- The Institute: word-by-word statement ---------------------------- */

  var statement = document.querySelector('.institute__statement');
  if (statement) {
    var words = statement.querySelectorAll('.word');
    if (prefersStatic() || !('IntersectionObserver' in window)) {
      words.forEach(function (w) { w.classList.add('is-lit'); });
    } else {
      var wordObserver = new IntersectionObserver(function (entries) {
        entries.forEach(function (entry) {
          if (!entry.isIntersecting) return;
          words.forEach(function (w, i) {
            setTimeout(function () { w.classList.add('is-lit'); }, i * 55);
          });
          wordObserver.disconnect();
        });
      }, { threshold: 0.3 });
      wordObserver.observe(statement);
    }
  }

  /* --- Hero: background parallax and drifting chips --------------------- */

  var heroBg = document.querySelector('.hero__bg');
  var chips = document.querySelectorAll('.chip');
  if ((heroBg || chips.length) && !reduceMotion.matches) {
    handlers.push(function () {
      var y = window.scrollY;
      if (y > window.innerHeight * 1.2) return;
      if (heroBg) heroBg.style.transform = 'translate3d(0,' + (y * 0.28).toFixed(1) + 'px,0)';
      // Each chip drifts at its own rate, so they separate as the page moves.
      chips.forEach(function (chip) {
        var speed = parseFloat(chip.getAttribute('data-speed')) || 0.12;
        chip.style.transform = 'translate3d(0,' + (-y * speed).toFixed(1) + 'px,0)';
      });
    });
  }

  /* --- Services: horizontal rail driven by vertical scroll -------------- */

  var services = document.querySelector('.services');
  if (services) {
    var scroller = services.querySelector('.services__scroll');
    var track = services.querySelector('.services__track');
    var bar = services.querySelector('.services__bar span');
    var count = services.querySelector('[data-svc-count]');
    var cards = track ? track.querySelectorAll('.service-card') : [];

    var updateRail = function () {
      if (prefersStatic() || !track || !scroller) return;
      var distance = scroller.offsetHeight - window.innerHeight;
      if (distance <= 0) return;

      // 0 when the section pins, 1 when it releases.
      var progress = Math.min(Math.max(-scroller.getBoundingClientRect().top / distance, 0), 1);

      // Slide the track just far enough that the last card ends flush.
      var overflow = track.scrollWidth - track.clientWidth;
      track.style.transform = 'translate3d(' + (-overflow * progress).toFixed(1) + 'px,0,0)';

      if (bar) bar.style.width = (progress * 100).toFixed(1) + '%';
      if (count && cards.length) {
        var index = Math.min(Math.round(progress * (cards.length - 1)) + 1, cards.length);
        count.textContent = String(index).padStart(2, '0');
      }
    };

    var syncRail = function () {
      var isStatic = prefersStatic();
      services.classList.toggle('services--static', isStatic);
      if (isStatic && track) track.style.transform = '';
      else updateRail();
    };

    handlers.push(updateRail);
    window.addEventListener('resize', syncRail);
    syncRail();
  }

  /* --- How we work: pinned step sequence -------------------------------- */

  var process = document.querySelector('.process');
  if (process) {
    var procScroller = process.querySelector('.process__scroll');
    var steps = process.querySelectorAll('.process__step');
    var medias = process.querySelectorAll('.process__media');
    var procCount = process.querySelector('[data-process-count]');

    var setStep = function (index) {
      steps.forEach(function (s, i) { s.classList.toggle('is-active', i === index); });
      medias.forEach(function (m, i) { m.classList.toggle('is-active', i === index); });
      if (procCount) procCount.textContent = String(index + 1);
    };

    var updateProcess = function () {
      if (prefersStatic() || !procScroller || !steps.length) return;
      var distance = procScroller.offsetHeight - window.innerHeight;
      if (distance <= 0) return;
      var progress = Math.min(Math.max(-procScroller.getBoundingClientRect().top / distance, 0), 1);
      setStep(Math.min(Math.floor(progress * steps.length), steps.length - 1));
    };

    var syncProcess = function () {
      var isStatic = prefersStatic();
      process.classList.toggle('process--static', isStatic);
      if (isStatic) steps.forEach(function (s) { s.classList.add('is-active'); });
      else updateProcess();
    };

    handlers.push(updateProcess);
    window.addEventListener('resize', syncProcess);
    syncProcess();
  }


  /* --- Reviews: fan the stacked cards out on reveal ---------------------- */

  var reviews = document.querySelector('.reviews');
  if (reviews) {
    var fanCards = reviews.querySelectorAll('.review');

    var layoutFan = function () {
      var isStatic = prefersStatic() || window.matchMedia('(max-width: 1100px)').matches;
      reviews.classList.toggle('reviews--static', isStatic);
      if (isStatic) {
        fanCards.forEach(function (c) { c.style.transform = ''; c.style.opacity = ''; });
      }
      return isStatic;
    };

    var fanOut = function () {
      if (layoutFan()) return;
      fanCards.forEach(function (card, i) {
        var rot = card.getAttribute('data-rot') || 0;
        var x = card.getAttribute('data-x') || 0;
        var y = card.getAttribute('data-y') || 0;
        setTimeout(function () {
          card.style.transform = 'translate(' + x + 'px,' + y + 'px) rotate(' + rot + 'deg)';
          card.style.opacity = '1';
        }, i * 90);
      });
    };

    if ('IntersectionObserver' in window) {
      var fanObserver = new IntersectionObserver(function (entries) {
        entries.forEach(function (entry) {
          if (!entry.isIntersecting) return;
          fanOut();
          fanObserver.disconnect();
        });
      }, { threshold: 0.2 });
      fanObserver.observe(reviews);
    } else {
      fanOut();
    }
    window.addEventListener('resize', layoutFan);
    layoutFan();
  }

  /* --- FAQ accordion ---------------------------------------------------- */

  var faqButtons = document.querySelectorAll('.faq__q');
  faqButtons.forEach(function (btn, i) {
    var panel = document.getElementById(btn.getAttribute('aria-controls'));
    if (!panel) return;
    // The canvas ships with the first question already open.
    if (i === 0) {
      btn.setAttribute('aria-expanded', 'true');
      requestAnimationFrame(function () { panel.style.height = panel.scrollHeight + 'px'; });
    } else {
      panel.style.height = '0px';
    }

    btn.addEventListener('click', function () {
      var isOpen = btn.getAttribute('aria-expanded') === 'true';

      // One open at a time, matching the canvas.
      faqButtons.forEach(function (other) {
        if (other === btn) return;
        var otherPanel = document.getElementById(other.getAttribute('aria-controls'));
        other.setAttribute('aria-expanded', 'false');
        if (otherPanel) otherPanel.style.height = '0px';
      });

      btn.setAttribute('aria-expanded', String(!isOpen));
      panel.style.height = isOpen ? '0px' : panel.scrollHeight + 'px';
    });
  });

  window.addEventListener('resize', function () {
    faqButtons.forEach(function (btn) {
      if (btn.getAttribute('aria-expanded') !== 'true') return;
      var panel = document.getElementById(btn.getAttribute('aria-controls'));
      if (panel) panel.style.height = panel.scrollHeight + 'px';
    });
  });

  /* --- Marquees: duplicate each group so the -50% loop is seamless ------ */

  document.querySelectorAll('.marquee__track').forEach(function (track) {
    var group = track.querySelector('.marquee__group');
    if (group) track.appendChild(group.cloneNode(true));
  });

  // Prime everything at the current scroll position.
  onScroll();
})();
