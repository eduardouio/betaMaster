/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}"
  ],
  daisyui: {
    themes: [
      {
        mytheme: {
          "primary": "#009ddf",
          "secondary": "#e0e0e0",
          "accent": "#94c200",
          "neutral": "#0c0902",
          "base-100": "#fffdfc",
          "info": "#008dff",
          "success": "#008260",
          "warning": "#e66000",
          "error": "#f5050e",
        },
      },
    ],
  },
  darkMode: 'class',
  theme: {
    extend: {
      backgroundColor: {
        'primary': '#3490dc',
        'secondary': '#00f0f0',
        'tertiary': '#ffed4a',
      },
      textColor: {
        'primary': '#3490dc',
        'secondary': '#ffed4a',
        'tertiary': '#ffed4a',
      }, fontFamily: {
        Montserrat: ['Montserrat', 'sans-serif'],
      },
    },
  },
  plugins: [
    require('daisyui'),
    require('@tailwindcss/aspect-ratio'),
  ],
}

