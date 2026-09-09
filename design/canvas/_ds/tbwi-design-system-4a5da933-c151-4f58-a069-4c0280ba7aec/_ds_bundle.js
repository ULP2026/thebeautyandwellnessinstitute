/* @ds-bundle: {"format":3,"namespace":"TBWIDesignSystem_4a5da9","components":[{"name":"ServiceCard","sourcePath":"components/brand/ServiceCard.jsx"},{"name":"Stat","sourcePath":"components/brand/Stat.jsx"},{"name":"Badge","sourcePath":"components/core/Badge.jsx"},{"name":"Button","sourcePath":"components/core/Button.jsx"},{"name":"Card","sourcePath":"components/core/Card.jsx"},{"name":"Eyebrow","sourcePath":"components/core/Eyebrow.jsx"},{"name":"Input","sourcePath":"components/forms/Input.jsx"},{"name":"Switch","sourcePath":"components/forms/Switch.jsx"}],"sourceHashes":{"components/brand/ServiceCard.jsx":"d5d017018416","components/brand/Stat.jsx":"4cffac681631","components/core/Badge.jsx":"8bce6ed17bcc","components/core/Button.jsx":"d8f47591c20d","components/core/Card.jsx":"d11264b3b06f","components/core/Eyebrow.jsx":"2742a6ca785c","components/forms/Input.jsx":"6c101eda623a","components/forms/Switch.jsx":"a384544d2fe0","ui_kits/website/AboutDr.jsx":"d93220e19e97","ui_kits/website/App.jsx":"c92b64f8f517","ui_kits/website/BookingScreen.jsx":"9ec41daf6e81","ui_kits/website/Hero.jsx":"5e28333ccc64","ui_kits/website/ServicesGrid.jsx":"c8eaa6d05159","ui_kits/website/SiteFooter.jsx":"78e8f56a0b4f","ui_kits/website/SiteHeader.jsx":"045dce9a56b6","ui_kits/website/TrustStrip.jsx":"c8bc63df0394"},"inlinedExternals":[],"unexposedExports":[]} */

(() => {

const __ds_ns = (window.TBWIDesignSystem_4a5da9 = window.TBWIDesignSystem_4a5da9 || {});

const __ds_scope = {};

(__ds_ns.__errors = __ds_ns.__errors || []);

// components/brand/ServiceCard.jsx
try { (() => {
function _extends() { return _extends = Object.assign ? Object.assign.bind() : function (n) { for (var e = 1; e < arguments.length; e++) { var t = arguments[e]; for (var r in t) ({}).hasOwnProperty.call(t, r) && (n[r] = t[r]); } return n; }, _extends.apply(null, arguments); }
/**
 * TBWI ServiceCard — the workhorse for treatment/service listings.
 * A botanical-framed icon slot, serif title, description, and quiet link.
 */
function ServiceCard({
  title,
  description,
  icon = null,
  category,
  href = '#',
  linkLabel = 'Learn more',
  style = {},
  ...rest
}) {
  return /*#__PURE__*/React.createElement("a", _extends({
    href: href,
    style: {
      display: 'flex',
      flexDirection: 'column',
      gap: '1rem',
      textDecoration: 'none',
      background: 'var(--surface-card)',
      border: '1px solid var(--border-subtle)',
      borderRadius: 'var(--radius-lg)',
      padding: 'var(--space-6)',
      boxShadow: 'var(--shadow-sm)',
      transition: 'box-shadow var(--dur-base) var(--ease-standard), transform var(--dur-base) var(--ease-standard)',
      ...style
    },
    onMouseEnter: e => {
      e.currentTarget.style.boxShadow = 'var(--shadow-lg)';
      e.currentTarget.style.transform = 'translateY(-3px)';
    },
    onMouseLeave: e => {
      e.currentTarget.style.boxShadow = 'var(--shadow-sm)';
      e.currentTarget.style.transform = 'translateY(0)';
    }
  }, rest), icon && /*#__PURE__*/React.createElement("span", {
    style: {
      display: 'inline-flex',
      alignItems: 'center',
      justifyContent: 'center',
      width: '52px',
      height: '68px',
      borderRadius: 'var(--radius-pill)',
      border: '1px solid var(--sage-300)',
      color: 'var(--sage-600)',
      background: 'var(--sage-50)'
    }
  }, icon), category && /*#__PURE__*/React.createElement("span", {
    style: {
      fontFamily: 'var(--font-body)',
      fontSize: 'var(--fs-xs)',
      fontWeight: 'var(--fw-medium)',
      letterSpacing: 'var(--tracking-eyebrow)',
      textTransform: 'uppercase',
      color: 'var(--accent)'
    }
  }, category), /*#__PURE__*/React.createElement("h3", {
    style: {
      fontFamily: 'var(--font-display)',
      fontWeight: 'var(--fw-semibold)',
      fontSize: 'var(--fs-h3)',
      color: 'var(--text-heading)',
      margin: 0,
      lineHeight: 'var(--lh-heading)'
    }
  }, title), /*#__PURE__*/React.createElement("p", {
    style: {
      fontFamily: 'var(--font-body)',
      fontSize: 'var(--fs-body)',
      color: 'var(--text-body)',
      margin: 0,
      lineHeight: 'var(--lh-body)',
      flex: 1
    }
  }, description), /*#__PURE__*/React.createElement("span", {
    style: {
      display: 'inline-flex',
      alignItems: 'center',
      gap: '0.4rem',
      fontFamily: 'var(--font-body)',
      fontSize: 'var(--fs-sm)',
      fontWeight: 'var(--fw-medium)',
      letterSpacing: 'var(--tracking-caps)',
      textTransform: 'uppercase',
      color: 'var(--text-link)'
    }
  }, linkLabel, " ", /*#__PURE__*/React.createElement("span", {
    "aria-hidden": "true"
  }, "\u2192")));
}
Object.assign(__ds_scope, { ServiceCard });
})(); } catch (e) { __ds_ns.__errors.push({ path: "components/brand/ServiceCard.jsx", error: String((e && e.message) || e) }); }

// components/brand/Stat.jsx
try { (() => {
function _extends() { return _extends = Object.assign ? Object.assign.bind() : function (n) { for (var e = 1; e < arguments.length; e++) { var t = arguments[e]; for (var r in t) ({}).hasOwnProperty.call(t, r) && (n[r] = t[r]); } return n; }, _extends.apply(null, arguments); }
/**
 * TBWI Stat — large serif figure with a quiet label. For trust strips.
 */
function Stat({
  value,
  label,
  align = 'center',
  style = {},
  ...rest
}) {
  return /*#__PURE__*/React.createElement("div", _extends({
    style: {
      display: 'flex',
      flexDirection: 'column',
      gap: '0.3rem',
      textAlign: align,
      alignItems: align === 'center' ? 'center' : 'flex-start',
      ...style
    }
  }, rest), /*#__PURE__*/React.createElement("span", {
    style: {
      fontFamily: 'var(--font-display)',
      fontWeight: 'var(--fw-semibold)',
      fontSize: 'var(--fs-display-3)',
      lineHeight: 1,
      color: 'var(--accent-strong)',
      letterSpacing: 'var(--tracking-tight)'
    }
  }, value), /*#__PURE__*/React.createElement("span", {
    style: {
      fontFamily: 'var(--font-body)',
      fontSize: 'var(--fs-sm)',
      letterSpacing: 'var(--tracking-wide)',
      color: 'var(--text-muted)'
    }
  }, label));
}
Object.assign(__ds_scope, { Stat });
})(); } catch (e) { __ds_ns.__errors.push({ path: "components/brand/Stat.jsx", error: String((e && e.message) || e) }); }

// components/core/Badge.jsx
try { (() => {
function _extends() { return _extends = Object.assign ? Object.assign.bind() : function (n) { for (var e = 1; e < arguments.length; e++) { var t = arguments[e]; for (var r in t) ({}).hasOwnProperty.call(t, r) && (n[r] = t[r]); } return n; }, _extends.apply(null, arguments); }
/**
 * TBWI Badge — small status/category pill.
 * tones: sage, teal, gold, neutral, success, warning, error.
 */
function Badge({
  children,
  tone = 'sage',
  subtle = true,
  style = {},
  ...rest
}) {
  const tones = {
    sage: {
      soft: {
        bg: 'var(--sage-100)',
        fg: 'var(--sage-700)'
      },
      solid: {
        bg: 'var(--sage-500)',
        fg: '#fff'
      }
    },
    teal: {
      soft: {
        bg: 'var(--teal-100)',
        fg: 'var(--teal-700)'
      },
      solid: {
        bg: 'var(--teal-500)',
        fg: '#fff'
      }
    },
    gold: {
      soft: {
        bg: 'var(--gold-300)',
        fg: 'var(--gold-700)'
      },
      solid: {
        bg: 'var(--gold-500)',
        fg: '#3A2F12'
      }
    },
    neutral: {
      soft: {
        bg: 'var(--greige-200)',
        fg: 'var(--ink-700)'
      },
      solid: {
        bg: 'var(--ink-700)',
        fg: '#fff'
      }
    },
    success: {
      soft: {
        bg: 'var(--success-bg)',
        fg: 'var(--success-fg)'
      },
      solid: {
        bg: 'var(--success-500)',
        fg: '#fff'
      }
    },
    warning: {
      soft: {
        bg: 'var(--warning-bg)',
        fg: 'var(--warning-fg)'
      },
      solid: {
        bg: 'var(--warning-500)',
        fg: '#fff'
      }
    },
    error: {
      soft: {
        bg: 'var(--error-bg)',
        fg: 'var(--error-fg)'
      },
      solid: {
        bg: 'var(--error-500)',
        fg: '#fff'
      }
    }
  };
  const c = tones[tone][subtle ? 'soft' : 'solid'];
  return /*#__PURE__*/React.createElement("span", _extends({
    style: {
      display: 'inline-flex',
      alignItems: 'center',
      gap: '0.35rem',
      padding: '0.25rem 0.7rem',
      background: c.bg,
      color: c.fg,
      fontFamily: 'var(--font-body)',
      fontSize: 'var(--fs-xs)',
      fontWeight: 'var(--fw-medium)',
      letterSpacing: 'var(--tracking-caps)',
      textTransform: 'uppercase',
      borderRadius: 'var(--radius-pill)',
      lineHeight: 1.4,
      ...style
    }
  }, rest), children);
}
Object.assign(__ds_scope, { Badge });
})(); } catch (e) { __ds_ns.__errors.push({ path: "components/core/Badge.jsx", error: String((e && e.message) || e) }); }

// components/core/Button.jsx
try { (() => {
function _extends() { return _extends = Object.assign ? Object.assign.bind() : function (n) { for (var e = 1; e < arguments.length; e++) { var t = arguments[e]; for (var r in t) ({}).hasOwnProperty.call(t, r) && (n[r] = t[r]); } return n; }, _extends.apply(null, arguments); }
/**
 * TBWI Button — calm, pill-shaped, generous padding.
 * Variants: primary (sage), secondary (teal outline), ghost, gold.
 */
function Button({
  children,
  variant = 'primary',
  size = 'md',
  fullWidth = false,
  disabled = false,
  iconLeft = null,
  iconRight = null,
  style = {},
  ...rest
}) {
  const sizes = {
    sm: {
      padding: '0.5rem 1.1rem',
      fontSize: 'var(--fs-sm)',
      gap: '0.4rem'
    },
    md: {
      padding: '0.75rem 1.6rem',
      fontSize: 'var(--fs-body)',
      gap: '0.55rem'
    },
    lg: {
      padding: '0.95rem 2.1rem',
      fontSize: 'var(--fs-lead)',
      gap: '0.6rem'
    }
  };
  const variants = {
    primary: {
      background: 'var(--brand)',
      color: 'var(--text-on-brand)',
      border: '1px solid var(--brand)'
    },
    secondary: {
      background: 'transparent',
      color: 'var(--accent-strong)',
      border: '1px solid var(--accent)'
    },
    ghost: {
      background: 'transparent',
      color: 'var(--text-body)',
      border: '1px solid transparent'
    },
    gold: {
      background: 'var(--gold-500)',
      color: '#3A2F12',
      border: '1px solid var(--gold-500)'
    }
  };
  const base = {
    display: fullWidth ? 'flex' : 'inline-flex',
    width: fullWidth ? '100%' : 'auto',
    alignItems: 'center',
    justifyContent: 'center',
    gap: sizes[size].gap,
    fontFamily: 'var(--font-body)',
    fontWeight: 'var(--fw-medium)',
    letterSpacing: 'var(--tracking-caps)',
    textTransform: 'uppercase',
    borderRadius: 'var(--radius-pill)',
    cursor: disabled ? 'not-allowed' : 'pointer',
    opacity: disabled ? 0.5 : 1,
    transition: 'all var(--dur-base) var(--ease-standard)',
    whiteSpace: 'nowrap',
    lineHeight: 1,
    ...sizes[size],
    ...variants[variant],
    ...style
  };
  return /*#__PURE__*/React.createElement("button", _extends({
    type: "button",
    disabled: disabled,
    style: base,
    onMouseEnter: e => {
      if (disabled) return;
      if (variant === 'primary') e.currentTarget.style.background = 'var(--brand-strong)';
      if (variant === 'secondary') {
        e.currentTarget.style.background = 'var(--accent-soft)';
      }
      if (variant === 'ghost') e.currentTarget.style.background = 'var(--surface-sunken)';
      if (variant === 'gold') e.currentTarget.style.background = 'var(--gold-700)';
      if (variant === 'gold') e.currentTarget.style.color = '#FFF';
    },
    onMouseLeave: e => {
      e.currentTarget.style.background = variants[variant].background;
      e.currentTarget.style.color = variants[variant].color;
    }
  }, rest), iconLeft, children, iconRight);
}
Object.assign(__ds_scope, { Button });
})(); } catch (e) { __ds_ns.__errors.push({ path: "components/core/Button.jsx", error: String((e && e.message) || e) }); }

// components/core/Card.jsx
try { (() => {
function _extends() { return _extends = Object.assign ? Object.assign.bind() : function (n) { for (var e = 1; e < arguments.length; e++) { var t = arguments[e]; for (var r in t) ({}).hasOwnProperty.call(t, r) && (n[r] = t[r]); } return n; }, _extends.apply(null, arguments); }
/**
 * TBWI Card — soft, ivory-white surface with diffuse shadow.
 * Optional accent rail and elevation levels.
 */
function Card({
  children,
  elevation = 'sm',
  padding = 'lg',
  interactive = false,
  style = {},
  ...rest
}) {
  const shadows = {
    none: 'none',
    xs: 'var(--shadow-xs)',
    sm: 'var(--shadow-sm)',
    md: 'var(--shadow-md)',
    lg: 'var(--shadow-lg)'
  };
  const pads = {
    none: '0',
    sm: 'var(--space-4)',
    md: 'var(--space-5)',
    lg: 'var(--space-6)'
  };
  return /*#__PURE__*/React.createElement("div", _extends({
    style: {
      background: 'var(--surface-card)',
      border: '1px solid var(--border-subtle)',
      borderRadius: 'var(--radius-lg)',
      boxShadow: shadows[elevation],
      padding: pads[padding],
      transition: 'box-shadow var(--dur-base) var(--ease-standard), transform var(--dur-base) var(--ease-standard)',
      cursor: interactive ? 'pointer' : 'default',
      ...style
    },
    onMouseEnter: interactive ? e => {
      e.currentTarget.style.boxShadow = 'var(--shadow-lg)';
      e.currentTarget.style.transform = 'translateY(-2px)';
    } : undefined,
    onMouseLeave: interactive ? e => {
      e.currentTarget.style.boxShadow = shadows[elevation];
      e.currentTarget.style.transform = 'translateY(0)';
    } : undefined
  }, rest), children);
}
Object.assign(__ds_scope, { Card });
})(); } catch (e) { __ds_ns.__errors.push({ path: "components/core/Card.jsx", error: String((e && e.message) || e) }); }

// components/core/Eyebrow.jsx
try { (() => {
function _extends() { return _extends = Object.assign ? Object.assign.bind() : function (n) { for (var e = 1; e < arguments.length; e++) { var t = arguments[e]; for (var r in t) ({}).hasOwnProperty.call(t, r) && (n[r] = t[r]); } return n; }, _extends.apply(null, arguments); }
/**
 * TBWI Eyebrow — the signature letter-spaced uppercase overline,
 * optionally flanked by a short botanical rule.
 */
function Eyebrow({
  children,
  rule = false,
  color = 'var(--accent)',
  style = {},
  ...rest
}) {
  return /*#__PURE__*/React.createElement("span", _extends({
    style: {
      display: 'inline-flex',
      alignItems: 'center',
      gap: '0.7rem',
      fontFamily: 'var(--font-body)',
      fontWeight: 'var(--fw-medium)',
      fontSize: 'var(--fs-eyebrow)',
      letterSpacing: 'var(--tracking-eyebrow)',
      textTransform: 'uppercase',
      color,
      ...style
    }
  }, rest), rule && /*#__PURE__*/React.createElement("span", {
    style: {
      width: '2rem',
      height: '1px',
      background: 'currentColor',
      opacity: 0.5
    }
  }), children, rule && /*#__PURE__*/React.createElement("span", {
    style: {
      width: '2rem',
      height: '1px',
      background: 'currentColor',
      opacity: 0.5
    }
  }));
}
Object.assign(__ds_scope, { Eyebrow });
})(); } catch (e) { __ds_ns.__errors.push({ path: "components/core/Eyebrow.jsx", error: String((e && e.message) || e) }); }

// components/forms/Input.jsx
try { (() => {
function _extends() { return _extends = Object.assign ? Object.assign.bind() : function (n) { for (var e = 1; e < arguments.length; e++) { var t = arguments[e]; for (var r in t) ({}).hasOwnProperty.call(t, r) && (n[r] = t[r]); } return n; }, _extends.apply(null, arguments); }
/**
 * TBWI Input — calm text field with label, optional hint/error.
 */
function Input({
  label,
  hint,
  error,
  type = 'text',
  id,
  style = {},
  ...rest
}) {
  const fieldId = id || `tbwi-input-${Math.random().toString(36).slice(2, 8)}`;
  return /*#__PURE__*/React.createElement("div", {
    style: {
      display: 'flex',
      flexDirection: 'column',
      gap: '0.4rem',
      width: '100%'
    }
  }, label && /*#__PURE__*/React.createElement("label", {
    htmlFor: fieldId,
    style: {
      fontFamily: 'var(--font-body)',
      fontSize: 'var(--fs-sm)',
      fontWeight: 'var(--fw-medium)',
      letterSpacing: 'var(--tracking-wide)',
      color: 'var(--text-body)'
    }
  }, label), /*#__PURE__*/React.createElement("input", _extends({
    id: fieldId,
    type: type,
    style: {
      fontFamily: 'var(--font-body)',
      fontSize: 'var(--fs-body)',
      color: 'var(--text-heading)',
      background: 'var(--surface-card)',
      border: `1px solid ${error ? 'var(--error-500)' : 'var(--border-default)'}`,
      borderRadius: 'var(--radius-md)',
      padding: '0.7rem 0.95rem',
      outline: 'none',
      transition: 'border-color var(--dur-fast) var(--ease-standard), box-shadow var(--dur-fast) var(--ease-standard)',
      ...style
    },
    onFocus: e => {
      e.currentTarget.style.borderColor = 'var(--border-focus)';
      e.currentTarget.style.boxShadow = 'var(--shadow-focus)';
    },
    onBlur: e => {
      e.currentTarget.style.borderColor = error ? 'var(--error-500)' : 'var(--border-default)';
      e.currentTarget.style.boxShadow = 'none';
    }
  }, rest)), (hint || error) && /*#__PURE__*/React.createElement("span", {
    style: {
      fontSize: 'var(--fs-xs)',
      color: error ? 'var(--error-fg)' : 'var(--text-muted)'
    }
  }, error || hint));
}
Object.assign(__ds_scope, { Input });
})(); } catch (e) { __ds_ns.__errors.push({ path: "components/forms/Input.jsx", error: String((e && e.message) || e) }); }

// components/forms/Switch.jsx
try { (() => {
function _extends() { return _extends = Object.assign ? Object.assign.bind() : function (n) { for (var e = 1; e < arguments.length; e++) { var t = arguments[e]; for (var r in t) ({}).hasOwnProperty.call(t, r) && (n[r] = t[r]); } return n; }, _extends.apply(null, arguments); }
/**
 * TBWI Switch — soft pill toggle in sage.
 */
function Switch({
  checked = false,
  onChange,
  label,
  disabled = false,
  style = {},
  ...rest
}) {
  return /*#__PURE__*/React.createElement("label", _extends({
    style: {
      display: 'inline-flex',
      alignItems: 'center',
      gap: '0.65rem',
      cursor: disabled ? 'not-allowed' : 'pointer',
      opacity: disabled ? 0.5 : 1,
      fontFamily: 'var(--font-body)',
      fontSize: 'var(--fs-sm)',
      color: 'var(--text-body)',
      ...style
    }
  }, rest), /*#__PURE__*/React.createElement("span", {
    onClick: () => !disabled && onChange && onChange(!checked),
    style: {
      position: 'relative',
      width: '44px',
      height: '26px',
      borderRadius: 'var(--radius-pill)',
      background: checked ? 'var(--brand)' : 'var(--greige-300)',
      transition: 'background var(--dur-base) var(--ease-standard)',
      flex: 'none'
    }
  }, /*#__PURE__*/React.createElement("span", {
    style: {
      position: 'absolute',
      top: '3px',
      left: checked ? '21px' : '3px',
      width: '20px',
      height: '20px',
      borderRadius: '50%',
      background: '#fff',
      boxShadow: 'var(--shadow-sm)',
      transition: 'left var(--dur-base) var(--ease-out)'
    }
  })), label && /*#__PURE__*/React.createElement("span", null, label));
}
Object.assign(__ds_scope, { Switch });
})(); } catch (e) { __ds_ns.__errors.push({ path: "components/forms/Switch.jsx", error: String((e && e.message) || e) }); }

// ui_kits/website/AboutDr.jsx
try { (() => {
// AboutDr — physician intro band on inverse teal surface.
function AboutDr() {
  const {
    Eyebrow,
    Button,
    Badge
  } = window.TBWIDesignSystem_4a5da9;
  return /*#__PURE__*/React.createElement("section", {
    style: {
      background: 'var(--surface-inverse)',
      color: 'var(--text-on-inverse)'
    }
  }, /*#__PURE__*/React.createElement("div", {
    style: {
      maxWidth: 'var(--container-max)',
      margin: '0 auto',
      padding: 'var(--space-9) var(--space-7)',
      display: 'grid',
      gridTemplateColumns: '0.85fr 1.15fr',
      gap: 'var(--space-8)',
      alignItems: 'center'
    }
  }, /*#__PURE__*/React.createElement("div", {
    style: {
      aspectRatio: '1 / 1',
      borderRadius: 'var(--radius-xl)',
      overflow: 'hidden',
      background: 'linear-gradient(160deg, var(--teal-500), var(--sage-500))',
      display: 'flex',
      alignItems: 'center',
      justifyContent: 'center',
      boxShadow: 'var(--shadow-lg)'
    }
  }, /*#__PURE__*/React.createElement("img", {
    src: "../../assets/logos/TBWI-logo-cream.png",
    alt: "",
    style: {
      width: '64%',
      opacity: 0.9
    }
  })), /*#__PURE__*/React.createElement("div", null, /*#__PURE__*/React.createElement(Eyebrow, {
    color: "var(--sage-300)"
  }, "Meet your physician"), /*#__PURE__*/React.createElement("h2", {
    style: {
      fontFamily: 'var(--font-display)',
      fontWeight: 500,
      fontSize: 'var(--fs-display-2)',
      color: '#fff',
      margin: '12px 0 18px',
      lineHeight: 1.1
    }
  }, "Dr. Pamela Chapman"), /*#__PURE__*/React.createElement("p", {
    style: {
      fontSize: 'var(--fs-lead)',
      fontWeight: 300,
      color: 'var(--text-on-inverse)',
      maxWidth: 520,
      margin: '0 0 20px'
    }
  }, "TBWI was founded on a simple belief: beauty and wellness are inseparable. Dr. Chapman builds each plan around your goals, treating appearance, health, and well-being as one."), /*#__PURE__*/React.createElement("div", {
    style: {
      display: 'flex',
      gap: 10,
      marginBottom: 26,
      flexWrap: 'wrap'
    }
  }, /*#__PURE__*/React.createElement(Badge, {
    tone: "sage",
    subtle: false
  }, "Board-certified"), /*#__PURE__*/React.createElement(Badge, {
    tone: "gold"
  }, "Physician-led"), /*#__PURE__*/React.createElement(Badge, {
    tone: "teal",
    subtle: false
  }, "Personalized care")), /*#__PURE__*/React.createElement(Button, {
    variant: "gold",
    size: "md"
  }, "Read her story"))));
}
window.AboutDr = AboutDr;
})(); } catch (e) { __ds_ns.__errors.push({ path: "ui_kits/website/AboutDr.jsx", error: String((e && e.message) || e) }); }

// ui_kits/website/App.jsx
try { (() => {
// App — composes the TBWI marketing site with simple view routing.
function App() {
  const [view, setView] = React.useState('home');
  const home = () => {
    setView('home');
    window.scrollTo(0, 0);
  };
  const book = () => {
    setView('booking');
    window.scrollTo(0, 0);
  };
  React.useEffect(() => {
    if (window.lucide) window.lucide.createIcons();
  }, [view]);
  return /*#__PURE__*/React.createElement("div", null, /*#__PURE__*/React.createElement(SiteHeader, {
    onBook: book,
    onHome: home
  }), view === 'home' ? /*#__PURE__*/React.createElement("main", null, /*#__PURE__*/React.createElement(Hero, {
    onBook: book
  }), /*#__PURE__*/React.createElement(TrustStrip, null), /*#__PURE__*/React.createElement(ServicesGrid, null), /*#__PURE__*/React.createElement(AboutDr, null)) : /*#__PURE__*/React.createElement("main", null, /*#__PURE__*/React.createElement(BookingScreen, {
    onHome: home
  })), /*#__PURE__*/React.createElement(SiteFooter, null));
}
window.App = App;
})(); } catch (e) { __ds_ns.__errors.push({ path: "ui_kits/website/App.jsx", error: String((e && e.message) || e) }); }

// ui_kits/website/BookingScreen.jsx
try { (() => {
// BookingScreen — consultation request form (the interactive second view).
function BookingScreen({
  onHome
}) {
  const {
    Input,
    Button,
    Eyebrow,
    Badge
  } = window.TBWIDesignSystem_4a5da9;
  const [submitted, setSubmitted] = React.useState(false);
  const [interest, setInterest] = React.useState('Aesthetics');
  const interests = ['Aesthetics', 'Wellness', 'Supplements', 'Not sure yet'];
  return /*#__PURE__*/React.createElement("div", {
    style: {
      maxWidth: 760,
      margin: '0 auto',
      padding: 'var(--space-9) var(--space-7)'
    }
  }, /*#__PURE__*/React.createElement("div", {
    style: {
      textAlign: 'center',
      marginBottom: 'var(--space-7)'
    }
  }, /*#__PURE__*/React.createElement(Eyebrow, {
    rule: true
  }, "Book a consultation"), /*#__PURE__*/React.createElement("h1", {
    style: {
      fontFamily: 'var(--font-display)',
      fontWeight: 600,
      fontSize: 'var(--fs-display-3)',
      color: 'var(--text-heading)',
      margin: '12px 0 8px'
    }
  }, "Start your plan with Dr. Chapman"), /*#__PURE__*/React.createElement("p", {
    style: {
      color: 'var(--text-muted)',
      margin: 0
    }
  }, "Tell us a little about you. We'll reach out within one business day.")), /*#__PURE__*/React.createElement("div", {
    style: {
      background: 'var(--surface-card)',
      border: '1px solid var(--border-subtle)',
      borderRadius: 'var(--radius-lg)',
      boxShadow: 'var(--shadow-md)',
      padding: 'var(--space-7)'
    }
  }, submitted ? /*#__PURE__*/React.createElement("div", {
    style: {
      textAlign: 'center',
      padding: 'var(--space-6) 0'
    }
  }, /*#__PURE__*/React.createElement("div", {
    style: {
      fontFamily: 'var(--font-display)',
      fontSize: 'var(--fs-h2)',
      color: 'var(--accent-strong)',
      marginBottom: 8
    }
  }, "Thank you."), /*#__PURE__*/React.createElement("p", {
    style: {
      color: 'var(--text-muted)',
      marginBottom: 24
    }
  }, "Your request is in. We'll be in touch shortly."), /*#__PURE__*/React.createElement(Button, {
    variant: "secondary",
    onClick: onHome
  }, "Back to home")) : /*#__PURE__*/React.createElement("form", {
    onSubmit: e => {
      e.preventDefault();
      setSubmitted(true);
    },
    style: {
      display: 'flex',
      flexDirection: 'column',
      gap: 'var(--space-5)'
    }
  }, /*#__PURE__*/React.createElement("div", {
    style: {
      display: 'grid',
      gridTemplateColumns: '1fr 1fr',
      gap: 'var(--space-5)'
    }
  }, /*#__PURE__*/React.createElement(Input, {
    label: "First name",
    placeholder: "Jane",
    required: true
  }), /*#__PURE__*/React.createElement(Input, {
    label: "Last name",
    placeholder: "Doe",
    required: true
  })), /*#__PURE__*/React.createElement("div", {
    style: {
      display: 'grid',
      gridTemplateColumns: '1fr 1fr',
      gap: 'var(--space-5)'
    }
  }, /*#__PURE__*/React.createElement(Input, {
    label: "Email",
    type: "email",
    placeholder: "jane@email.com",
    required: true
  }), /*#__PURE__*/React.createElement(Input, {
    label: "Phone",
    type: "tel",
    placeholder: "(555) 012-3456"
  })), /*#__PURE__*/React.createElement("div", null, /*#__PURE__*/React.createElement("div", {
    style: {
      fontFamily: 'var(--font-body)',
      fontSize: 'var(--fs-sm)',
      fontWeight: 500,
      color: 'var(--text-body)',
      marginBottom: 10
    }
  }, "I'm interested in"), /*#__PURE__*/React.createElement("div", {
    style: {
      display: 'flex',
      gap: 10,
      flexWrap: 'wrap'
    }
  }, interests.map(i => /*#__PURE__*/React.createElement("button", {
    type: "button",
    key: i,
    onClick: () => setInterest(i),
    style: {
      cursor: 'pointer',
      padding: '0.4rem 0.9rem',
      borderRadius: 'var(--radius-pill)',
      fontFamily: 'var(--font-body)',
      fontSize: 'var(--fs-sm)',
      letterSpacing: 'var(--tracking-caps)',
      textTransform: 'uppercase',
      border: `1px solid ${interest === i ? 'var(--brand)' : 'var(--border-default)'}`,
      background: interest === i ? 'var(--brand)' : 'transparent',
      color: interest === i ? '#fff' : 'var(--text-body)',
      transition: 'all var(--dur-fast) var(--ease-standard)'
    }
  }, i)))), /*#__PURE__*/React.createElement(Input, {
    label: "Anything we should know?",
    placeholder: "Optional"
  }), /*#__PURE__*/React.createElement("div", {
    style: {
      display: 'flex',
      justifyContent: 'space-between',
      alignItems: 'center',
      marginTop: 4
    }
  }, /*#__PURE__*/React.createElement(Button, {
    variant: "ghost",
    type: "button",
    onClick: onHome
  }, "Cancel"), /*#__PURE__*/React.createElement(Button, {
    variant: "primary",
    size: "lg",
    type: "submit"
  }, "Request consultation")))));
}
window.BookingScreen = BookingScreen;
})(); } catch (e) { __ds_ns.__errors.push({ path: "ui_kits/website/BookingScreen.jsx", error: String((e && e.message) || e) }); }

// ui_kits/website/Hero.jsx
try { (() => {
// Hero — full-width split hero with serif headline and image placeholder.
function Hero({
  onBook
}) {
  const {
    Eyebrow,
    Button
  } = window.TBWIDesignSystem_4a5da9;
  return /*#__PURE__*/React.createElement("section", {
    style: {
      display: 'grid',
      gridTemplateColumns: '1.05fr 0.95fr',
      alignItems: 'center',
      gap: 'var(--space-8)',
      padding: 'var(--space-9) var(--space-7)',
      maxWidth: 'var(--container-max)',
      margin: '0 auto'
    }
  }, /*#__PURE__*/React.createElement("div", null, /*#__PURE__*/React.createElement(Eyebrow, {
    rule: false
  }, "The Beauty & Wellness Institute"), /*#__PURE__*/React.createElement("h1", {
    style: {
      fontFamily: 'var(--font-display)',
      fontWeight: 600,
      fontSize: 'clamp(2.8rem, 5vw, 4.4rem)',
      lineHeight: 1.04,
      color: 'var(--text-heading)',
      margin: '14px 0 18px',
      letterSpacing: '-.01em'
    }
  }, "Look and feel your best, ", /*#__PURE__*/React.createElement("span", {
    style: {
      fontStyle: 'italic',
      color: 'var(--accent-strong)'
    }
  }, "from the inside out.")), /*#__PURE__*/React.createElement("p", {
    style: {
      fontSize: 'var(--fs-lead)',
      fontWeight: 300,
      color: 'var(--text-body)',
      maxWidth: 460,
      margin: '0 0 28px'
    }
  }, "Aesthetic treatments and medical wellness care, thoughtfully combined and personalized to you by Dr. Pamela Chapman."), /*#__PURE__*/React.createElement("div", {
    style: {
      display: 'flex',
      gap: 'var(--space-3)'
    }
  }, /*#__PURE__*/React.createElement(Button, {
    variant: "primary",
    size: "lg",
    onClick: onBook
  }, "Book a consultation"), /*#__PURE__*/React.createElement(Button, {
    variant: "secondary",
    size: "lg"
  }, "Explore services"))), /*#__PURE__*/React.createElement("div", {
    style: {
      position: 'relative',
      aspectRatio: '4 / 5',
      borderRadius: 'var(--radius-xl)',
      background: 'linear-gradient(150deg, var(--sage-200), var(--teal-200))',
      overflow: 'hidden',
      boxShadow: 'var(--shadow-lg)',
      display: 'flex',
      alignItems: 'center',
      justifyContent: 'center'
    }
  }, /*#__PURE__*/React.createElement("img", {
    src: "../../assets/logos/TBWI-logo-cream.png",
    alt: "",
    style: {
      width: '62%',
      opacity: 0.92
    }
  }), /*#__PURE__*/React.createElement("span", {
    style: {
      position: 'absolute',
      bottom: 14,
      right: 16,
      fontFamily: 'var(--font-mono)',
      fontSize: 11,
      color: 'rgba(255,255,255,.7)'
    }
  }, "clinic imagery")));
}
window.Hero = Hero;
})(); } catch (e) { __ds_ns.__errors.push({ path: "ui_kits/website/Hero.jsx", error: String((e && e.message) || e) }); }

// ui_kits/website/ServicesGrid.jsx
try { (() => {
function _extends() { return _extends = Object.assign ? Object.assign.bind() : function (n) { for (var e = 1; e < arguments.length; e++) { var t = arguments[e]; for (var r in t) ({}).hasOwnProperty.call(t, r) && (n[r] = t[r]); } return n; }, _extends.apply(null, arguments); }
// ServicesGrid — the four pillars of TBWI care.
function ServicesGrid() {
  const {
    ServiceCard,
    Eyebrow
  } = window.TBWIDesignSystem_4a5da9;
  const Icon = ({
    n
  }) => /*#__PURE__*/React.createElement("i", {
    "data-lucide": n,
    style: {
      width: 22,
      height: 22,
      strokeWidth: 1.5
    }
  });
  const items = [{
    category: 'Aesthetics',
    title: 'Botox & Fillers',
    description: 'Smooth fine lines and restore volume with precise, natural-looking results.',
    icon: 'sparkles'
  }, {
    category: 'Aesthetics',
    title: 'Sculptra & Hair',
    description: 'Collagen-stimulating treatments and restoration for skin and hair.',
    icon: 'flower-2'
  }, {
    category: 'Wellness',
    title: 'Hormone & Weight',
    description: 'Hormone therapy, weight management, and peptides tailored to your biology.',
    icon: 'heart-pulse'
  }, {
    category: 'Wellness',
    title: 'IV Therapy',
    description: 'Targeted hydration and nutrient infusions to support energy and recovery.',
    icon: 'droplet'
  }, {
    category: 'Supplements',
    title: 'Medical-Grade',
    description: 'Professional supplements prescribed and delivered through Fullscript.',
    icon: 'pill'
  }, {
    category: 'Care',
    title: 'Consultation',
    description: 'A 1:1 plan with Dr. Chapman, mapping aesthetics and wellness together.',
    icon: 'calendar-heart'
  }];
  React.useEffect(() => {
    if (window.lucide) window.lucide.createIcons();
  });
  return /*#__PURE__*/React.createElement("section", {
    style: {
      maxWidth: 'var(--container-max)',
      margin: '0 auto',
      padding: 'var(--space-9) var(--space-7)'
    }
  }, /*#__PURE__*/React.createElement("div", {
    style: {
      textAlign: 'center',
      marginBottom: 'var(--space-7)'
    }
  }, /*#__PURE__*/React.createElement(Eyebrow, {
    rule: true
  }, "What we offer"), /*#__PURE__*/React.createElement("h2", {
    style: {
      fontFamily: 'var(--font-display)',
      fontWeight: 600,
      fontSize: 'var(--fs-display-3)',
      color: 'var(--text-heading)',
      margin: '12px 0 0'
    }
  }, "Four pillars of beauty & wellness")), /*#__PURE__*/React.createElement("div", {
    style: {
      display: 'grid',
      gridTemplateColumns: 'repeat(3, 1fr)',
      gap: 'var(--space-5)'
    }
  }, items.map(it => /*#__PURE__*/React.createElement(ServiceCard, _extends({
    key: it.title
  }, it, {
    icon: /*#__PURE__*/React.createElement(Icon, {
      n: it.icon
    })
  })))));
}
window.ServicesGrid = ServicesGrid;
})(); } catch (e) { __ds_ns.__errors.push({ path: "ui_kits/website/ServicesGrid.jsx", error: String((e && e.message) || e) }); }

// ui_kits/website/SiteFooter.jsx
try { (() => {
// SiteFooter — calm footer with logo, columns, fine print.
function SiteFooter() {
  const cols = [{
    h: 'Aesthetics',
    links: ['Botox & Fillers', 'Sculptra', 'Hair Restoration']
  }, {
    h: 'Wellness',
    links: ['Hormone Therapy', 'Weight Management', 'Peptides', 'IV Therapy']
  }, {
    h: 'Institute',
    links: ['About Dr. Chapman', 'Supplements', 'Book a Visit', 'Contact']
  }];
  return /*#__PURE__*/React.createElement("footer", {
    style: {
      background: 'var(--surface-sunken)',
      borderTop: '1px solid var(--border-subtle)'
    }
  }, /*#__PURE__*/React.createElement("div", {
    style: {
      maxWidth: 'var(--container-max)',
      margin: '0 auto',
      padding: 'var(--space-8) var(--space-7)',
      display: 'grid',
      gridTemplateColumns: '1.4fr repeat(3, 1fr)',
      gap: 'var(--space-6)'
    }
  }, /*#__PURE__*/React.createElement("div", null, /*#__PURE__*/React.createElement("img", {
    src: "../../assets/logos/TBWI-logo-sage.png",
    alt: "TBWI",
    style: {
      height: 76,
      marginBottom: 12
    }
  }), /*#__PURE__*/React.createElement("p", {
    style: {
      fontSize: 'var(--fs-sm)',
      color: 'var(--text-muted)',
      maxWidth: 240,
      margin: 0
    }
  }, "The Beauty & Wellness Institute \xB7 Dr. Pamela Chapman")), cols.map(c => /*#__PURE__*/React.createElement("div", {
    key: c.h
  }, /*#__PURE__*/React.createElement("div", {
    style: {
      fontFamily: 'var(--font-body)',
      fontSize: 'var(--fs-xs)',
      fontWeight: 600,
      letterSpacing: 'var(--tracking-eyebrow)',
      textTransform: 'uppercase',
      color: 'var(--accent)',
      marginBottom: 14
    }
  }, c.h), /*#__PURE__*/React.createElement("ul", {
    style: {
      listStyle: 'none',
      margin: 0,
      padding: 0,
      display: 'flex',
      flexDirection: 'column',
      gap: 10
    }
  }, c.links.map(l => /*#__PURE__*/React.createElement("li", {
    key: l
  }, /*#__PURE__*/React.createElement("a", {
    href: "#",
    style: {
      fontSize: 'var(--fs-sm)',
      color: 'var(--text-body)',
      textDecoration: 'none'
    }
  }, l))))))), /*#__PURE__*/React.createElement("div", {
    style: {
      borderTop: '1px solid var(--border-subtle)',
      padding: 'var(--space-4) var(--space-7)',
      maxWidth: 'var(--container-max)',
      margin: '0 auto',
      display: 'flex',
      justifyContent: 'space-between'
    }
  }, /*#__PURE__*/React.createElement("span", {
    style: {
      fontSize: 'var(--fs-xs)',
      color: 'var(--text-subtle)'
    }
  }, "\xA9 2026 The Beauty & Wellness Institute. All rights reserved."), /*#__PURE__*/React.createElement("span", {
    style: {
      fontSize: 'var(--fs-xs)',
      color: 'var(--text-subtle)'
    }
  }, "Privacy \xB7 Terms")));
}
window.SiteFooter = SiteFooter;
})(); } catch (e) { __ds_ns.__errors.push({ path: "ui_kits/website/SiteFooter.jsx", error: String((e && e.message) || e) }); }

// ui_kits/website/SiteHeader.jsx
try { (() => {
// SiteHeader — sticky top nav for the TBWI marketing site.
function SiteHeader({
  onBook,
  onHome
}) {
  const nav = ['Aesthetics', 'Wellness', 'Supplements', 'About'];
  return /*#__PURE__*/React.createElement("header", {
    style: {
      position: 'sticky',
      top: 0,
      zIndex: 50,
      display: 'flex',
      alignItems: 'center',
      justifyContent: 'space-between',
      padding: '0 var(--space-7)',
      height: 76,
      background: 'color-mix(in srgb, var(--surface-canvas) 88%, transparent)',
      backdropFilter: 'blur(10px)',
      borderBottom: '1px solid var(--border-subtle)'
    }
  }, /*#__PURE__*/React.createElement("div", {
    onClick: onHome,
    style: {
      display: 'flex',
      alignItems: 'center',
      gap: 12,
      cursor: 'pointer'
    }
  }, /*#__PURE__*/React.createElement("img", {
    src: "../../assets/logos/TBWI-logo-sage.png",
    alt: "TBWI",
    style: {
      height: 46
    }
  }), /*#__PURE__*/React.createElement("span", {
    style: {
      fontFamily: 'var(--font-display)',
      fontSize: 22,
      fontWeight: 600,
      color: 'var(--text-heading)',
      letterSpacing: '.01em'
    }
  }, "Dr. Pamela Chapman")), /*#__PURE__*/React.createElement("nav", {
    style: {
      display: 'flex',
      gap: 'var(--space-6)'
    }
  }, nav.map(n => /*#__PURE__*/React.createElement("a", {
    key: n,
    href: "#",
    style: {
      fontFamily: 'var(--font-body)',
      fontSize: 'var(--fs-sm)',
      fontWeight: 500,
      letterSpacing: 'var(--tracking-caps)',
      textTransform: 'uppercase',
      color: 'var(--text-body)',
      textDecoration: 'none'
    }
  }, n))), /*#__PURE__*/React.createElement(Button, {
    size: "sm",
    onClick: onBook
  }, "Book a consultation"));
}
window.SiteHeader = SiteHeader;
})(); } catch (e) { __ds_ns.__errors.push({ path: "ui_kits/website/SiteHeader.jsx", error: String((e && e.message) || e) }); }

// ui_kits/website/TrustStrip.jsx
try { (() => {
// TrustStrip — quiet stat row beneath the hero.
function TrustStrip() {
  const {
    Stat
  } = window.TBWIDesignSystem_4a5da9;
  const sep = () => /*#__PURE__*/React.createElement("div", {
    style: {
      width: 1,
      alignSelf: 'stretch',
      background: 'var(--border-default)'
    }
  });
  return /*#__PURE__*/React.createElement("section", {
    style: {
      background: 'var(--surface-sunken)',
      borderBlock: '1px solid var(--border-subtle)'
    }
  }, /*#__PURE__*/React.createElement("div", {
    style: {
      maxWidth: 880,
      margin: '0 auto',
      padding: 'var(--space-6) var(--space-7)',
      display: 'flex',
      alignItems: 'center',
      gap: 'var(--space-6)',
      justifyContent: 'space-between'
    }
  }, /*#__PURE__*/React.createElement(Stat, {
    value: "15+",
    label: "Years in practice"
  }), sep(), /*#__PURE__*/React.createElement(Stat, {
    value: "4",
    label: "Pillars of care"
  }), sep(), /*#__PURE__*/React.createElement(Stat, {
    value: "98%",
    label: "Would recommend"
  }), sep(), /*#__PURE__*/React.createElement(Stat, {
    value: "1:1",
    label: "Physician-led plans"
  })));
}
window.TrustStrip = TrustStrip;
})(); } catch (e) { __ds_ns.__errors.push({ path: "ui_kits/website/TrustStrip.jsx", error: String((e && e.message) || e) }); }

__ds_ns.ServiceCard = __ds_scope.ServiceCard;

__ds_ns.Stat = __ds_scope.Stat;

__ds_ns.Badge = __ds_scope.Badge;

__ds_ns.Button = __ds_scope.Button;

__ds_ns.Card = __ds_scope.Card;

__ds_ns.Eyebrow = __ds_scope.Eyebrow;

__ds_ns.Input = __ds_scope.Input;

__ds_ns.Switch = __ds_scope.Switch;

})();
