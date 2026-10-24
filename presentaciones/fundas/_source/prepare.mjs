import{existsSync,cpSync,mkdirSync,copyFileSync}from'node:fs';
if(!existsSync('public/images')){if(!existsSync('../images'))throw Error('Faltan imágenes: conservar _source junto al directorio publicado images.');mkdirSync('public',{recursive:true});cpSync('../images','public/images',{recursive:true});}

if(!existsSync('public/Fundas-textiles-peruanas.pdf')&&existsSync('../Fundas-textiles-peruanas.pdf'))copyFileSync('../Fundas-textiles-peruanas.pdf','public/Fundas-textiles-peruanas.pdf');
