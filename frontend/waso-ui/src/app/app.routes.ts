import { Routes } from '@angular/router';
import { Home } from './components/home/home'; // Verify this folder path matches yours!
import { Gallery } from './components/gallery/gallery';

export const routes: Routes = [
  // This tells Angular: when a user lands on the site, load the Home component instantly
  { path: 'home', component: Home },
  
  // Placeholders for your other paths
  { path: 'gallery', component: Gallery },
  { path: 'testimonials', component: Home },
  { path: 'book', component: Home },
  { path: 'login', component: Home }
];