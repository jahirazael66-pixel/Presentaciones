import{existsSync,cpSync,mkdirSync,copyFileSync}from'node:fs';
if(!existsSync('public/assets/images')){if(!existsSync('../assets/images'))throw Error('Conservar _source junto al directorio publicado assets/images.');mkdirSync('public/assets',{recursive:true});cpSync('../assets/images','public/assets/images',{recursive:true});}
if(!existsSync('public/Greenbox-Triple-Impacto-2027.pdf')&&existsSync('../Greenbox-Triple-Impacto-2027.pdf'))copyFileSync('../Greenbox-Triple-Impacto-2027.pdf','public/Greenbox-Triple-Impacto-2027.pdf');
