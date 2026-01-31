/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './templates/**/*.{html,js}',          // Django template files
    './**/templates/**/*.{html,js}',
    './static/src/**/*.{css,js}',          // যদি CSS/JS ফাইল থেকে class use করো
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}
