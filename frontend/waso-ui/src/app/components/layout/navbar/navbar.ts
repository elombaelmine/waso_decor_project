import { Component, signal } from '@angular/core';
import { RouterLink, RouterLinkActive } from '@angular/router'; // Add this line

@Component({
  selector: 'app-navbar',
  standalone: true,
  imports: [RouterLink, RouterLinkActive], // Add them here
  templateUrl: './navbar.html',
  styleUrl: './navbar.css'
})
export class Navbar {
  protected readonly isLoggedIn = signal<boolean>(false);

  protected onLogout(): void {
    this.isLoggedIn.set(false);
    console.log('User logged out successfully.');
  }
}