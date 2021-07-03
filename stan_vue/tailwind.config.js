module.exports = {
  purge: { content: ['./public/**/*.html', './src/**/*.vue'] },
  darkMode: false, // or 'media' or 'class'
  theme: {
    extend: {
      fontFamily:{
        body:['Montserrat'],
        apex:['Apex Mk3 ExtraLight'],
        apexm:['Apex Mk3 Medium'],
        nunito:['Nunito Sans']
      },
    },
  },
  variants: {
    extend: {},
  },
  plugins: [],
}
