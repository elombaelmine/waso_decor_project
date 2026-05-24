import { Component, signal, computed } from '@angular/core';
import { FormsModule } from '@angular/forms';

interface Message {
  id: number;
  sender: 'client' | 'manager';
  text: string;
  timestamp: string;
}

@Component({
  selector: 'app-chat',
  standalone: true,
  imports: [FormsModule],
  templateUrl: './chat.html',
  styleUrl: './chat.css'
})
export class Chat {
  // Track active navigation panel target view
  protected readonly activeTab = signal<'chat' | 'inquiry'>('chat');

  // Chat Subsystem Signals
  protected readonly newMessageText = signal<string>('');
  protected readonly messageLog = signal<Message[]>([
    { id: 1, sender: 'manager', text: 'Hello! Welcome to Waso Deco. How can we help design your upcoming atmosphere?', timestamp: '10:30 AM' }
  ]);

  // Inquiry Form Parameter Signals
  protected readonly eventType = signal<string>('');
  protected readonly eventDate = signal<string>('');
  protected readonly guestCount = signal<string>('');
  protected readonly colorPalette = signal<string>('');
  protected readonly specificDetails = signal<string>('');
  protected readonly inquirySubmitted = signal<boolean>(false);

  protected switchView(target: 'chat' | 'inquiry'): void {
    this.activeTab.set(target);
    if (target === 'inquiry') {
      this.inquirySubmitted.set(false); // Reset form state if toggled back
    }
  }

  protected dispatchChatMessage(): void {
    if (!this.newMessageText().trim()) return;

    const userMsg: Message = {
      id: Date.now(),
      sender: 'client',
      text: this.newMessageText().trim(),
      timestamp: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })
    };

    this.messageLog.update(logs => [...logs, userMsg]);
    this.newMessageText.set('');

    // Simulate design manager auto-response pipeline
    setTimeout(() => {
      const managerMsg: Message = {
        id: Date.now() + 1,
        sender: 'manager',
        text: 'Thank you for your response. Our design panel is reviewing your request notes right now.',
        timestamp: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })
      };
      this.messageLog.update(logs => [...logs, managerMsg]);
    }, 1500);
  }

  protected sendInquiryForm(): void {
    console.log('Sending structured event inquiry parameters to Django:', {
      type: this.eventType(),
      date: this.eventDate(),
      guests: this.guestCount(),
      colors: this.colorPalette(),
      notes: this.specificDetails()
    });

    this.inquirySubmitted.set(true);
    
    // Clear inputs after submission
    this.eventType.set('');
    this.eventDate.set('');
    this.guestCount.set('');
    this.colorPalette.set('');
    this.specificDetails.set('');
  }
}