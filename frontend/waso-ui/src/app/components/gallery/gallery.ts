import { Component, OnInit, inject, signal } from '@angular/core';
import { HttpClient } from '@angular/common/http';

// 1. The Blueprint: Must match the exact field outputs from your Django Serializer
interface GalleryItem {
  id: number;
  title: string;          // Matches your Django model 'Title'
  image: string;          // Matches your Django model 'Image' (URL string format)
  event_type: string;     // Matches your Django model 'Event type'
  primary_color: string;  // Matches your Django model 'Primary color'
}

@Component({
  selector: 'app-gallery',
  standalone: true,
  imports: [], 
  templateUrl: './gallery.html',
  styleUrl: './gallery.css'
})
export class Gallery implements OnInit {
  // 2. Inject Angular's HTTP tool to make background data calls
  private http = inject(HttpClient);
  
  // 3. Initialize your array signal as empty. Django will fill this dynamically!
  protected readonly galleryItems = signal<GalleryItem[]>([]);

  ngOnInit(): void {
    this.fetchAdminUploads();
  }

  private fetchAdminUploads(): void {
    // 4. Point this string to your local running Python Django server API endpoint!
    // Change this string if your local API path uses a different URL segment (like '/api/gallery-items/')
    this.http.get<GalleryItem[]>('http://127.0.0.1:8000/api/gallery/')
      .subscribe({
        next: (data) => {
          this.galleryItems.set(data); // Screen instantly paints your real uploaded admin pictures!
        },
        error: (err) => {
          console.error('Could not load data entries from the Django server:', err);
        }
      });
  }
}