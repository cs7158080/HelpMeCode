import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { TagService } from './services/tag/tag.service';
import { HomeComponent } from './components/home/home.component';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet ],
  providers: [TagService,HomeComponent],
  templateUrl: './app.component.html',
  styleUrl: './app.component.scss'
})
export class AppComponent {
  title = 'angular';
}
