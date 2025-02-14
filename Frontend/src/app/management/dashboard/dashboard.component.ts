import { Component, OnInit } from '@angular/core';
import { AuthService } from '../../shared/services/auth.service';
import { CommonModule } from '@angular/common';  
@Component({
  selector: 'app-dashboard',
  imports: [CommonModule],
  templateUrl: './dashboard.component.html',
  styleUrl: './dashboard.component.css'
})
export class DashboardComponent implements OnInit {

  userRole: string = '';  // Para almacenar el rol del usuario
  isAdmin: boolean = false;
  isModerator: boolean = false;

  constructor(private authService: AuthService) {}

  ngOnInit(): void {
    // Suponiendo que tienes un token JWT con el rol del usuario
    const token = localStorage.getItem('token');
    if (token) {
      const decodedToken = this.decodeToken(token);
      this.userRole = decodedToken.role;
      this.isAdmin = this.userRole === 'admin';
      this.isModerator = this.userRole === 'moderator';
    }
  }

  // Función para decodificar el token (esto depende de cómo hayas generado el token en el backend)
  decodeToken(token: string): any {
    const payload = atob(token.split('.')[1]);  // Decodifica el payload del JWT
    return JSON.parse(payload);
  }
}
