import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { environment } from '../../environments/environment.prod';
import { tap } from 'rxjs/operators';  // Importamos 'tap'

@Injectable({
  providedIn: 'root'
})
export class AuthService {

  private apiUrl = `${environment.apiUrl}/login`;  // URL del backend (Flask)

  constructor(private http: HttpClient) { }

  login(username: string, password: string): Observable<any> {
    const credentials = { username, password };

    // Log para verificar que la solicitud se está realizando
    console.log('Enviando solicitud a la API con los siguientes datos:', credentials);

    return this.http.post<any>(this.apiUrl, credentials).pipe(
      tap({
        next: (response: any) => {
          console.log('Respuesta de la API:', response);  // Log de respuesta exitosa
        },
        error: (error: any) => {
          console.error('Error al hacer la solicitud HTTP:', error);  // Log de error si la API no responde
        }
      })
    );
  }
}
