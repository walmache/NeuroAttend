import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root',
})
export class TokenService {
  constructor() {}

  // Función para obtener el token desde localStorage
  getToken(): string | null {
    return localStorage.getItem('token');
  }

  // Función para decodificar el token
  decodeToken(token: string): any {
    try {
      const payload = atob(token.split('.')[1]);  // Decodifica el payload del JWT
      return JSON.parse(payload);
    } catch (error) {
      console.error('Error al decodificar el token:', error);
      return null;
    }
  }

  // Función para obtener el rol del usuario
  getRole(): string | null {
    const token = this.getToken();
    if (token) {
      const decodedToken = this.decodeToken(token);
      return decodedToken ? decodedToken.role : null;
    }
    return null;
  }

  // Función para verificar si el usuario es administrador
  isAdmin(): boolean {
    return this.getRole() === 'admin';
  }

  // Función para verificar si el usuario es moderador
  isModerator(): boolean {
    return this.getRole() === 'moderator';
  }
}
