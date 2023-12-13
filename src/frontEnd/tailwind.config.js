/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}"
  ],
  darkMode: 'class',
  theme: {
    extend: {
      backgroundColor:{
        'primary': '#3490dc',
        'secondary': '#00f0f0',
        'tertiary': '#ffed4a',
      },
      textColor:{
        'primary': '#3490dc',
        'secondary': '#ffed4a',
        'tertiary': '#ffed4a',
      },fontFamily:{
        Montserrat: ['Montserrat', 'sans-serif'],
      },
    },
  },
  plugins: [
    require('daisyui'),
    require('@tailwindcss/aspect-ratio'),
  ],
}

