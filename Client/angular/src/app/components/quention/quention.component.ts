import { Component, OnInit } from '@angular/core';
import { QuentionService } from '../../services/quention/quention.service'; 
import { Question } from '../../modules/interfaces';
import { QuentionDetailsComponent } from '../quention-details/quention-details.component';
import { CommonModule } from '@angular/common'; 

@Component({
  selector: 'app-quention',
  imports: [CommonModule,QuentionDetailsComponent],
  templateUrl: './quention.component.html',
  styleUrls: ['./quention.component.scss']
})
export class QuentionComponent implements OnInit {
  quentions: Question[] = [];

  constructor(private quentionService: QuentionService) { }

  ngOnInit(): void {
    this.loadQuentions();
  }

  loadQuentions(): void {
    this.quentionService.getAllQuentions().subscribe((data: Question[]) => {
      this.quentions = data;
    });
  }
}
