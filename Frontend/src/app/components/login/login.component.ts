import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { Router } from '@angular/router';
import { AuthService } from '../../services/auth.service';

@Component({
  selector: 'app-login',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent {
  usuario = '';;
  password = '';
  errorMessage = '';

  constructor(private authService: AuthService, private router: Router) {}

  login() {
    this.authService.login(this.usuario, this.password).subscribe({
      next: (response) => {
        localStorage.setItem('token', response.token);
        localStorage.setItem('rol', response.rol); // Guardar el rol
        

        // Redirigir según el rol
        switch (response.rol) {
          case 'administrador':
            this.router.navigate(['/dashboard']);
            break;
          case 'moderador':
            this.router.navigate(['/reuniones']);
            break;
          case 'usuario':
            this.router.navigate(['/bienvenida']);
            break;
          default:
            this.errorMessage = 'Rol no reconocido';
        }
      },
      error: (err) => {
        this.errorMessage = err.error.message || 'Error en la autenticación';
      }
    });
  }
}