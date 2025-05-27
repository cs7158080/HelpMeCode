import { Component, OnInit } from '@angular/core';
import { AnswerService } from '../../services/answer/answer.service';
import { Answer } from '../../modules/interfaces'; 
import { CommonModule } from '@angular/common';
import { AnswerDetailsComponent } from '../answer-details/answer-details.component';

@Component({
  selector: 'app-answer',
  imports: [CommonModule,AnswerDetailsComponent],
  templateUrl: './answer.component.html',
  styleUrls: ['./answer.component.scss']
})
export class AnswerComponent implements OnInit {
  answers: Answer[] = [];

  constructor(private answerService: AnswerService) { }

  ngOnInit(): void {
    this.loadAnswers();
  }

  loadAnswers(): void {
    this.answerService.getAllAnswers().subscribe((data: Answer[]) => {
      this.answers = data;
    });
  }
}
