import { Component, OnInit } from '@angular/core';
import { UserService } from '../../services/user/user.service';
import { User } from '../../modules/interfaces';
import { CommonModule } from '@angular/common';


@Component({
  selector: 'app-user',
  imports: [CommonModule],
  standalone: true,
  templateUrl: './user.component.html',
  styleUrls: ['./user.component.scss'],

})
export class UserComponent implements OnInit {
  users: User[] = [];

  constructor(private userService: UserService) { }

  ngOnInit(): void {
    this.loadUsers();
  }

  loadUsers(): void {
    this.userService.getAllUsers().subscribe(
      (data: User[]) => {
        this.users = data;
      },
      (error) => {
        console.error('Error fetching users:', error);
      }
    );
  }
    loadUsersByName(name: string): void {
    this.userService.getUsersByName(name).subscribe(
      (data: User) => {
        this.users = [data];
      },
      (error) => {
        console.error('Error fetching user by name:', error);
      }
    );
  }

  loadUsersByTags(tags: string[]): void {
    this.userService.getUsersByTags(tags).subscribe(
      (data: User[]) => {
        this.users = data;
      },
      (error) => {
        console.error('Error fetching users by tags:', error);
      }
    );
  }


  
  loadUsersByTagsTrue(tags: string[]): void {
    this.userService.getUsersByTagsTrue(tags).subscribe(
      (data: User[]) => {
        this.users = data;
      },
      (error) => {
        console.error('Error fetching users by tags true:', error);
      }
    );
  }

  loadUsersByTagsFalse(tags: string[]): void {
    this.userService.getUsersByTagsFalse(tags).subscribe(
      (data: User[]) => {
        this.users = data;
      },
      (error) => {
        console.error('Error fetching users by tags false:', error);
      }
    );
  }


}

