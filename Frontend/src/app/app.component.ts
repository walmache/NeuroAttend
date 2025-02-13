import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { SidebarComponent } from './admin-lte/sidebar/sidebar.component';
import { LayoutComponent } from './admin-lte/layout/layout.component';
import { HeaderComponent } from './admin-lte/header/header.component';
import { FooterComponent } from './admin-lte/footer/footer.component';

@Component({
  selector: 'app-root',
  imports: [
    RouterOutlet,
    SidebarComponent,
    LayoutComponent,
    HeaderComponent,
    FooterComponent
  ],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {
  title = 'Frontend';
}
