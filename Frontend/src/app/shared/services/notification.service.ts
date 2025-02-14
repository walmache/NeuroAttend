import { Injectable } from '@angular/core';
import Swal from 'sweetalert2';  // Importar SweetAlert2

@Injectable({
  providedIn: 'root',
})
export class NotificationService {

  constructor() { }

  showMessage(type: 'success' | 'error' | 'info' | 'warning', message: string) {
    // Mapeamos el tipo de mensaje y mostramos la alerta correspondiente
    Swal.fire({
      icon: type,  // Icono basado en el tipo
      title: this.getTitle(type),  // Título basado en el tipo
      text: message,  // El mensaje que se pasa desde el componente
    });
  }

  // Función para determinar el título según el tipo de mensaje
  private getTitle(type: 'success' | 'error' | 'info' | 'warning'): string {
    switch (type) {
      case 'success': return 'Éxito';
      case 'error': return 'Error';
      case 'info': return 'Información';
      case 'warning': return 'Advertencia';
      default: return '';
    }
  }
}
