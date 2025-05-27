import { Component, OnInit } from '@angular/core';
import { TagService } from '../../services/tag/tag.service';
import { Tag } from '../../modules/interfaces';
import { TagDetailsComponent } from '../tag-details/tag-details.component';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-tag',
   imports: [CommonModule,TagDetailsComponent],
  templateUrl: './tag.component.html',
  styleUrls: ['./tag.component.scss']
})
export class TagComponent implements OnInit {
  tags: Tag[] = [];

  constructor(private tagService: TagService) { }

  ngOnInit(): void {
    this.loadTags();
  }

  loadTags(): void {
    this.tagService.getAllTags().subscribe((data: Tag[]) => {
      this.tags = data;
    });
  }
}
