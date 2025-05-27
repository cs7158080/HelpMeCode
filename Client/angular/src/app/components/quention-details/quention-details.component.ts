import { Component, Input } from '@angular/core';
import { Question } from '../../modules/interfaces';

@Component({
  selector: 'app-quention-details',
  templateUrl: './quention-details.component.html',
  styleUrls: ['./quention-details.component.scss']
})
export class QuentionDetailsComponent {
  @Input() quention!: Question;
}
