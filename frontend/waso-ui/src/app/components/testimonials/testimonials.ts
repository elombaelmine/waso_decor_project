import { Component, OnInit, inject, signal, computed } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { RouterModule } from '@angular/router'; // Import this to handle link redirections

interface Testimonial {
  id: number;
  client_name: string;
  content: string; 
  is_visible: boolean; 
}

@Component({
  selector: 'app-testimonials',
  standalone: true,
  imports: [RouterModule], // Added here so routerLink works inside the template
  templateUrl: './testimonials.html',
  styleUrl: './testimonials.css'
})
export class Testimonials implements OnInit {
  private http = inject(HttpClient);
  
  // 1. Dynamic Authentication state toggle tracker
  // Set this to 'true' to see the textbox, or 'false' to test the hidden guest prompt!
  protected readonly isLoggedIn = signal<boolean>(false);

  private readonly allTestimonials = signal<Testimonial[]>([]);

  protected readonly visibleTestimonials = computed(() => {
    return this.allTestimonials().filter(t => t.is_visible);
  });

  ngOnInit(): void {
    this.fetchTestimonials();
  }

  private fetchTestimonials(): void {
    this.http.get<Testimonial[]>('http://127.0.0.1:8000/api/testimonials/')
      .subscribe({
        next: (data) => this.allTestimonials.set(data),
        error: (err) => console.error('Could not load testimonials from Django:', err)
      });
  }
}