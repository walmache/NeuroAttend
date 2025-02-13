import { bootstrapApplication } from '@angular/platform-browser';
import { AppComponent } from './app/app.component';
import { provideRouter } from '@angular/router';  // Importar `provideRouter`
import { routes } from './app/app.routes';  // Asegúrate de que la ruta a `app.routes.ts` sea correcta

bootstrapApplication(AppComponent, {
  providers: [
    provideRouter(routes),  // Configuramos el enrutador con `provideRouter`
  ]
});
