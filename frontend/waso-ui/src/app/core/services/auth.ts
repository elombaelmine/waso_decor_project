import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable, tap } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class Auth {
  // Pointing directly to your local Django Dev server
  private baseUrl = 'http://127.0.0.1:8000/api/auth';

  constructor(private http: HttpClient) {}

  /**
   * 1. Public Client Sign-Up Registration Gateway
   */
  signUp(userData: { fullName: string; email: string; password: string }): Observable<any> {
    return this.http.post(`${this.baseUrl}/sign-up/`, userData);
  }

  /**
   * 2. Transactional OTP Code Token Verification
   */
  verifyOtp(otpData: { email: string; verificationCode: string }): Observable<any> {
    return this.http.post(`${this.baseUrl}/otp-verify/`, otpData);
  }

  /**
   * 3. Secure JWT Token Login Gateway
   */
  login(credentials: { username: string; password: string }): Observable<any> {
    return this.http.post<any>(`${this.baseUrl}/login/`, credentials).pipe(
      tap(response => {
        // Securely holds token keys in the client browser across page reloads
        if (response && response.access) {
          localStorage.setItem('waso_access_token', response.access);
          localStorage.setItem('waso_refresh_token', response.refresh);
          localStorage.setItem('waso_user_email', credentials.username);
        }
      })
    );
  }

  /**
   * Helper utility to wipe session keys during sign out
   */
  logout(): void {
    localStorage.clear();
  }
}