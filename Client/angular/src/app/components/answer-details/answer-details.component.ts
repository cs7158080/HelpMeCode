import { Component, Input } from '@angular/core';
import { Answer } from '../../modules/interfaces'; // ודא שיש לך ממשק Answer

@Component({
  selector: 'app-answer-details',
  templateUrl: './answer-details.component.html',
  styleUrls: ['./answer-details.component.scss']
})
export class AnswerDetailsComponent {
  @Input() answer!: Answer;
}
