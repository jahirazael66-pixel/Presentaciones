import{existsSync,cpSync,mkdirSync}from'node:fs';
if(!existsSync('public/images')){if(!existsSync('../images'))throw Error('Faltan imágenes: conservar _source junto al directorio publicado images.');mkdirSync('public',{recursive:true});cpSync('../images','public/images',{recursive:true});}
