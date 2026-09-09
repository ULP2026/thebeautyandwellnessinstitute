/* ==========================================================================
   TBWI — home page behaviour.

   Everything here is progressive enhancement. The page is readable and
   complete with this file absent: index.html carries a `no-js` class that
   this script removes on load, and the CSS uses `.no-js` to fall back to
   plain stacked layouts for the two scroll-driven sections.

   Anyone who prefers reduced motion gets the same static fallbacks, applied
   here as .services--static / .process--static.
   ========================================================================== */

(function () {
  'use strict';

  var root = document.documentElement;
  root.classList.remove('no-js');

  var reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
  var narrow = window.matchMedia('(max-width: 900px)');

  function prefersStatic() {
    return reduceMotion.matches || narrow.matches;
  }

  /* --- Header: solid once the hero is behind us ------------------------ */

  var header = document.querySelector('.site-header');
  if (header) {
    var onScrollHeader = function () {
      header.classList.toggle('is-stuck', window.scrollY > 40);
    };
    onScrollHeader();
    window.addEventListener('scroll', onScrollHeader, { passive: true });
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

    // Any link inside closes it, since every link is an in-page anchor.
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

  /* --- Scroll reveal --------------------------------------------------- */

  var revealables = document.querySelectorAll('.reveal');
  if (revealables.length && 'IntersectionObserver' in window) {
    var revealObserver = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        entry.target.classList.add('is-visible');
        revealObserver.unobserve(entry.target);
      });
    }, { rootMargin: '0px 0px -12% 0px', threshold: 0.1 });

    revealables.forEach(function (el) { revealObserver.observe(el); });
  } else {
    revealables.forEach(function (el) { el.classList.add('is-visible'); });
  }

  /* --- The Institute: word-by-word statement --------------------------- */

  var statement = document.querySelector('.institute__statement');
  if (statement && 'IntersectionObserver' in window) {
    var words = statement.querySelectorAll('.word');

    if (prefersStatic()) {
      words.forEach(function (w) { w.classList.add('is-lit'); });
    } else {
      var wordObserver = new IntersectionObserver(function (entries) {
        entries.forEach(function (entry) {
          if (!entry.isIntersecting) return;
          words.forEach(function (w, i) {
            setTimeout(function () { w.classList.add('is-lit'); }, i * 45);
          });
          wordObserver.disconnect();
        });
      }, { threshold: 0.35 });
      wordObserver.observe(statement);
    }
  }

  /* --- Hero parallax --------------------------------------------------- */

  var heroBg = document.querySelector('.hero__bg');
  if (heroBg && !reduceMotion.matches) {
    var heroTicking = false;
    var moveHero = function () {
      var y = window.scrollY;
      if (y < window.innerHeight * 1.2) {
        heroBg.style.transform = 'translate3d(0,' + (y * 0.18).toFixed(1) + 'px,0)';
      }
      heroTicking = false;
    };
    window.addEventListener('scroll', function () {
      if (heroTicking) return;
      heroTicking = true;
      requestAnimationFrame(moveHero);
    }, { passive: true });
  }

  /* --- Services: horizontal rail driven by vertical scroll ------------- */

  var services = document.querySelector('.services');
  if (services) {
    var scroller = services.querySelector('.services__scroll');
    var track = services.querySelector('.services__track');
    var current = services.querySelector('.services__counter strong');
    var cards = track ? track.querySelectorAll('.service-card') : [];

    var railTicking = false;

    var updateRail = function () {
      railTicking = false;
      if (prefersStatic() || !track || !scroller) return;

      var rect = scroller.getBoundingClientRect();
      var distance = scroller.offsetHeight - window.innerHeight;
      if (distance <= 0) return;

      // 0 at the moment the section pins, 1 when it releases.
      var progress = Math.min(Math.max(-rect.top / distance, 0), 1);

      // Slide the track just far enough that the last card ends flush right.
      var overflow = track.scrollWidth - track.clientWidth;
      track.style.transform = 'translate3d(' + (-overflow * progress).toFixed(1) + 'px,0,0)';

      if (current && cards.length) {
        var index = Math.min(Math.round(progress * (cards.length - 1)) + 1, cards.length);
        current.textContent = String(index).padStart(2, '0');
      }
    };

    var onRailScroll = function () {
      if (railTicking) return;
      railTicking = true;
      requestAnimationFrame(updateRail);
    };

    var syncRailMode = function () {
      services.classList.toggle('services--static', prefersStatic());
      if (prefersStatic() && track) track.style.transform = '';
      else updateRail();
    };

    syncRailMode();
    window.addEventListener('scroll', onRailScroll, { passive: true });
    window.addEventListener('resize', syncRailMode);
  }

  /* --- How we work: pinned step sequence -------------------------------- */

  var process = document.querySelector('.process');
  if (process) {
    var procScroller = process.querySelector('.process__scroll');
    var steps = process.querySelectorAll('.process__step');
    var dots = process.querySelectorAll('.process__dot');
    var procTicking = false;

    var setStep = function (index) {
      steps.forEach(function (s, i) { s.classList.toggle('is-active', i === index); });
      dots.forEach(function (d, i) { d.classList.toggle('is-active', i === index); });
    };

    var updateProcess = function () {
      procTicking = false;
      if (prefersStatic() || !procScroller || !steps.length) return;

      var rect = procScroller.getBoundingClientRect();
      var distance = procScroller.offsetHeight - window.innerHeight;
      if (distance <= 0) return;

      var progress = Math.min(Math.max(-rect.top / distance, 0), 1);
      // Nudge just shy of the end so the final step holds while the section releases.
      var index = Math.min(Math.floor(progress * steps.length), steps.length - 1);
      setStep(index);
    };

    var onProcScroll = function () {
      if (procTicking) return;
      procTicking = true;
      requestAnimationFrame(updateProcess);
    };

    var syncProcessMode = function () {
      var isStatic = prefersStatic();
      process.classList.toggle('process--static', isStatic);
      if (isStatic) {
        steps.forEach(function (s) { s.classList.remove('is-active'); });
      } else {
        updateProcess();
      }
    };

    syncProcessMode();
    window.addEventListener('scroll', onProcScroll, { passive: true });
    window.addEventListener('resize', syncProcessMode);
  }

  /* --- FAQ accordion ---------------------------------------------------- */

  var faqButtons = document.querySelectorAll('.faq__q');
  faqButtons.forEach(function (btn) {
    var panel = document.getElementById(btn.getAttribute('aria-controls'));
    if (!panel) return;

    // Collapsed to start; CSS animates the explicit height we set here.
    panel.style.height = '0px';

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

  // Keep an open answer the right height when the text reflows.
  window.addEventListener('resize', function () {
    faqButtons.forEach(function (btn) {
      if (btn.getAttribute('aria-expanded') !== 'true') return;
      var panel = document.getElementById(btn.getAttribute('aria-controls'));
      if (panel) panel.style.height = panel.scrollHeight + 'px';
    });
  });

  /* --- Marquees: duplicate the track so the loop is seamless ----------- */

  document.querySelectorAll('.marquee__track').forEach(function (track) {
    track.innerHTML += track.innerHTML;
  });
})();
