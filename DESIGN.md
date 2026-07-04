---
name: Clinical Elite Narrative
colors:
  surface: '#f9f9fc'
  surface-dim: '#dadadd'
  surface-bright: '#f9f9fc'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f3f3f6'
  surface-container: '#eeedf1'
  surface-container-high: '#e8e8eb'
  surface-container-highest: '#e2e2e5'
  on-surface: '#1a1c1e'
  on-surface-variant: '#42474e'
  inverse-surface: '#2f3033'
  inverse-on-surface: '#f1f0f4'
  outline: '#72777e'
  outline-variant: '#c2c7ce'
  surface-tint: '#396285'
  primary: '#00263f'
  on-primary: '#ffffff'
  primary-container: '#0b3c5d'
  on-primary-container: '#7fa7cd'
  inverse-primary: '#a3cbf2'
  secondary: '#006a68'
  on-secondary: '#ffffff'
  secondary-container: '#86f4f1'
  on-secondary-container: '#00706f'
  tertiary: '#371d00'
  on-tertiary: '#ffffff'
  tertiary-container: '#553001'
  on-tertiary-container: '#ce9760'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#cee5ff'
  primary-fixed-dim: '#a3cbf2'
  on-primary-fixed: '#001d32'
  on-primary-fixed-variant: '#1f4a6c'
  secondary-fixed: '#86f4f1'
  secondary-fixed-dim: '#69d8d5'
  on-secondary-fixed: '#00201f'
  on-secondary-fixed-variant: '#00504f'
  tertiary-fixed: '#ffdcbd'
  tertiary-fixed-dim: '#f6bb80'
  on-tertiary-fixed: '#2c1600'
  on-tertiary-fixed-variant: '#663e0e'
  background: '#f9f9fc'
  on-background: '#1a1c1e'
  surface-variant: '#e2e2e5'
typography:
  display:
    fontFamily: manrope
    fontSize: 48px
    fontWeight: '800'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  h1:
    fontFamily: manrope
    fontSize: 32px
    fontWeight: '700'
    lineHeight: '1.2'
  h2:
    fontFamily: manrope
    fontSize: 24px
    fontWeight: '700'
    lineHeight: '1.3'
  h3:
    fontFamily: manrope
    fontSize: 20px
    fontWeight: '600'
    lineHeight: '1.4'
  body-lg:
    fontFamily: inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  label-bold:
    fontFamily: inter
    fontSize: 14px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: 0.01em
  caption:
    fontFamily: inter
    fontSize: 12px
    fontWeight: '500'
    lineHeight: '1.2'
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 40px
  xxl: 64px
  section: 112px
---

## Brand & Style

This design system establishes a high-trust, prestigious environment for international medical recruitment. The aesthetic merges the efficiency of high-end SaaS with the sobriety of corporate healthcare. By prioritizing a **Minimalist-Modern** style, the interface reduces cognitive load for busy medical professionals while maintaining a premium feel.

The brand personality is authoritative yet empathetic—human-centric imagery should be paired with precise, technical layouts. The emotional response is one of "calm confidence," achieved through generous whitespace, a sophisticated cool-toned palette, and a refined sense of depth.

## Colors

The color strategy uses **Deep Blue (#0B3C5D)** as the anchor for trust and institutional authority. **Secondary Teal (#2CA6A4)** provides a fresh, clinical vitality used for secondary actions and success states. **Accent Orange (#F4A261)** is reserved strictly for high-priority calls to action and notifications to ensure visibility without breaking the professional harmony.

Backgrounds utilize a "Paper-on-Cloud" approach: clean white surfaces resting on a very light gray foundation to create subtle structural differentiation without heavy lines.

## Typography

This design system pairs **Manrope** for headings and **Inter** for body copy. Manrope’s geometric yet warm proportions lend an "innovative medical" feel to titles, while Inter’s exceptional legibility handles dense recruitment data and candidate CVs with ease.

Headings should be bold and impactful to create a clear information hierarchy. Body text utilizes a generous 1.6 line-height to ensure comfort during long reading sessions, such as reviewing contract details or job descriptions.

## Layout & Spacing

The design system employs a **Fixed Grid** model for desktop to maintain a premium, editorial feel, transitioning to a fluid model for tablet and mobile. A strict 8px spatial rhythm governs all padding and margins.

Emphasis is placed on "Macro-whitespace"—using larger gaps (64px+) between sections to allow the content to breathe. This spacing strategy prevents the recruitment platform from feeling cluttered or overwhelming, reinforcing the "Elite" brand positioning.

## Elevation & Depth

Visual hierarchy is conveyed through **Ambient Shadows** and tonal layering. Surfaces do not use harsh borders; instead, depth is created using extremely soft, diffused shadows (Blur: 20px-40px) with a subtle tint of the primary blue (#0B3C5D) at 4-6% opacity.

- **Level 0 (Base):** Subtle light gray background.
- **Level 1 (Cards):** White surfaces with soft shadows.
- **Level 2 (Modals/Popovers):** Higher elevation with a semi-transparent backdrop blur (12px) to maintain context.

This "Soft-SaaS" approach creates a sense of tactile quality and modern sophistication.

## Shapes

The shape language is defined by **Large Rounded Corners**, moving away from clinical sharpness toward a more approachable, human-centric form. Main container elements (Cards, Dashboards) use a 20px radius. Functional elements like inputs and buttons use a 12px radius to maintain a cohesive, "friendly professional" look. Icons should follow this logic, utilizing rounded caps and joins rather than sharp angles.

## Components

- **Buttons:** Primary buttons use the Deep Blue with white text. Secondary buttons use a Teal ghost style (Teal border/text). Hover states should involve a subtle upward lift (elevation increase) rather than just a color shift.
- **Input Fields:** Large 12px rounded corners with a 1px border in a soft gray. On focus, the border transitions to Teal with a subtle outer glow.
- **Cards:** White background, 20px corner radius, and a soft ambient shadow. Cards are used to encapsulate candidate profiles and job listings.
- **Chips/Badges:** Used for medical specialties (e.g., "Cardiology"). These should have 100px (pill) radius, utilizing low-saturation versions of the secondary teal or primary blue to keep the UI quiet.
- **Recruitment Timeline:** A custom component representing the hiring stages. It should use thin lines and soft "node" circles, highlighting the current stage in Teal.
- **Status Indicators:** Use small, soft-colored dots (Success: Teal, Warning: Orange, Neutral: Gray) next to text labels for a clean, non-distracting status overview.