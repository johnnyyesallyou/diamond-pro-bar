/** @type {import('tailwindcss').Config} */
export default {
	content: ['./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}'],
	theme: {
		extend: {
			colors: {
				gold: '#D4AF37',
				'gold-dark': '#AA8C2C',
				'dark-bg': '#0A0E27',
				'dark-card': '#1A1F3A',
				'dark-border': '#2D3748',
				neon: '#00FF88',
				'neon-pink': '#FF006E',
			},
			fontFamily: {
				serif: ['Playfair Display', 'serif'],
				sans: ['Inter', 'sans-serif'],
			},
			animation: {
				'fade-in': 'fadeIn 0.6s ease-in-out',
				'slide-up': 'slideUp 0.6s ease-out',
				'fade-in-up': 'fadeInUp 0.8s ease-out',
			},
			keyframes: {
				fadeIn: {
					'0%': { opacity: '0' },
					'100%': { opacity: '1' },
				},
				slideUp: {
					'0%': { transform: 'translateY(30px)', opacity: '0' },
					'100%': { transform: 'translateY(0)', opacity: '1' },
				},
				fadeInUp: {
					'0%': { transform: 'translateY(40px)', opacity: '0' },
					'100%': { transform: 'translateY(0)', opacity: '1' },
				},
			},
			backgroundImage: {
				'gradient-gold': 'linear-gradient(135deg, #D4AF37 0%, #AA8C2C 100%)',
				'gradient-dark': 'linear-gradient(180deg, #0A0E27 0%, #1A1F3A 100%)',
				'gradient-neon': 'linear-gradient(135deg, #00FF88 0%, #FF006E 100%)',
			},
		},
	},
	plugins: [
		require('@tailwindcss/typography'),
		require('@tailwindcss/aspect-ratio'),
	],
};
