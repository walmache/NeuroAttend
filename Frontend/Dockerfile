# Usar una imagen base de Node.js versión 11.13.1
FROM node:22.13.1

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar los archivos de dependencias
COPY package.json package-lock.json ./

# Instalar dependencias
RUN npm install

# Copiar el resto del código
COPY . .

# Exponer el puerto 4200
EXPOSE 4200

# Comando para iniciar la aplicación
#CMD ["npm", "start"]
CMD ["npm", "start", "--", "--host", "0.0.0.0", "--port", "4200", "--disable-host-check"]
