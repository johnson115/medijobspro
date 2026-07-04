/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./*.html", "./js/**/*.js"],
  darkMode: "class",
  theme: {
    extend: {
      colors: {
        "on-primary-fixed-variant": "#1f4a6c", "surface-dim": "#dadadd", "primary-fixed": "#cee5ff",
        "tertiary-fixed-dim": "#f6bb80", "on-tertiary-fixed-variant": "#663e0e", "error-container": "#ffdad6",
        "error": "#ba1a1a", "inverse-on-surface": "#f1f0f4", "on-surface": "#1a1c1e",
        "on-primary-container": "#7fa7cd", "surface-container": "#eeedf1", "tertiary-container": "#553001",
        "on-primary": "#ffffff", "surface-bright": "#f9f9fc", "on-secondary-fixed": "#2a200d",
        "on-error": "#ffffff", "tertiary": "#371d00", "surface-container-lowest": "#ffffff",
        "on-secondary-container": "#4f3d1b", "outline-variant": "#c2c7ce", "inverse-primary": "#a3cbf2",
        "background": "#f9f9fc", "primary-container": "#0b3c5d", "on-secondary": "#ffffff",
        "outline": "#72777e", "primary": "#00263f", "on-tertiary-fixed": "#2c1600",
        "on-tertiary": "#ffffff", "tertiary-fixed": "#ffdcbd", "on-background": "#1a1c1e",
        "on-tertiary-container": "#ce9760", "secondary": "#c9a76f", "primary-fixed-dim": "#a3cbf2",
        "surface-container-high": "#e8e8eb", "secondary-fixed": "#eed6b4", "surface-container-low": "#f3f3f6",
        "secondary-fixed-dim": "#dcb883", "surface-tint": "#396285", "surface-container-highest": "#e2e2e5",
        "surface-variant": "#e2e2e5", "on-surface-variant": "#42474e", "inverse-surface": "#2f3033",
        "on-primary-fixed": "#001d32", "on-secondary-fixed-variant": "#4f3d1b",
        "secondary-container": "#eed6b4", "on-error-container": "#93000a", "surface": "#f9f9fc"
      },
      borderRadius: { DEFAULT: "0.25rem", lg: "0.5rem", xl: "0.75rem", full: "9999px" },
      spacing: { section: "112px", xxl: "64px", xs: "4px", xl: "40px", sm: "8px", lg: "24px", md: "16px" },
      fontFamily: { "label-bold": ["Inter"], caption: ["Inter"], "body-md": ["Inter"], h3: ["Manrope"], h2: ["Manrope"], display: ["Manrope"], "body-lg": ["Inter"], h1: ["Manrope"] },
      fontSize: {
        "label-bold": ["14px", { lineHeight: "1.2", letterSpacing: "0.01em", fontWeight: "600" }],
        caption: ["12px", { lineHeight: "1.2", fontWeight: "500" }],
        "body-md": ["16px", { lineHeight: "1.6", fontWeight: "400" }],
        h3: ["20px", { lineHeight: "1.4", fontWeight: "600" }],
        h2: ["24px", { lineHeight: "1.3", fontWeight: "700" }],
        display: ["48px", { lineHeight: "1.1", letterSpacing: "-0.02em", fontWeight: "800" }],
        "body-lg": ["18px", { lineHeight: "1.6", fontWeight: "400" }],
        h1: ["32px", { lineHeight: "1.2", fontWeight: "700" }]
      }
    }
  },
  plugins: [
    require('@tailwindcss/forms'),
    require('@tailwindcss/container-queries')
  ]
}
