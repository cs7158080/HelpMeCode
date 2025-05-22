import { Component, Input } from '@angular/core';
import { User } from '../../modules/interfaces';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-user-details',
  imports: [CommonModule],
  standalone: true,
  templateUrl: './user-details.component.html',
  styleUrls: ['./user-details.component.scss']
})
export class UserDetailsComponent {
  @Input() user!: User; 
}
