import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { environment } from '../../../environments/environment';
import { tap } from 'rxjs/operators';  

@Injectable({
  providedIn: 'root'
})
export class AuthService {

  private apiUrl = `${environment.apiUrl}/clientes/login`; 

  constructor(private http: HttpClient) { }

  login(usuario: string, password: string): Observable<any> {
    const credentials = { usuario, password };
    console.log('Enviando solicitud a la API con los siguientes datos:', credentials);
    return this.http.post<any>(this.apiUrl, credentials).pipe(
      tap({
        next: (response: any) => {
          console.log('Respuesta de la API:', response);  
        },
        error: (error: any) => {
          console.error('Error al hacer la solicitud HTTP:', error); 
        }
      })
    );
  }
}
