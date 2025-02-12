import { Injectable, inject } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';
import { environment } from '../../environments/environment';

@Injectable({
  providedIn: 'root'
})
export class AuthService {
  
  private apiUrl = environment.apiUrl;

  private http = inject(HttpClient);

  login(usuario: string, password: string): Observable<any> {
    const headers = new HttpHeaders({ 'Content-Type': 'application/json' });
    const body = JSON.stringify({ usuario, password }); // Convertir datos a JSON correctamente

    return this.http.post(`${this.apiUrl}/login`, body, { headers });
  }

  logout(): void {
    localStorage.removeItem('token');
    localStorage.removeItem('rol');
  }

  getUserRole(): string | null {
    return localStorage.getItem('rol');
  }
  isAuthenticated(): boolean {
    return !!localStorage.getItem('token');
  }
}

