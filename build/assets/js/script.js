// script.js - Consent Mode V2 e Interações Globais

// Google Consent Mode v2 default setup (injected in head, but logic here for the banner)
window.dataLayer = window.dataLayer || [];
function gtag(){dataLayer.push(arguments);}

document.addEventListener('DOMContentLoaded', function() {
    const consentBanner = document.getElementById('lgpd-banner');
    const btnAccept = document.getElementById('btn-accept-cookies');
    const btnReject = document.getElementById('btn-reject-cookies');

    // Check localStorage
    const consentStatus = localStorage.getItem('consentStatus');
    
    if (!consentStatus) {
        consentBanner.style.display = 'flex'; // Show banner
    } else if (consentStatus === 'granted') {
        gtag('consent', 'update', {
            'ad_storage': 'granted',
            'ad_user_data': 'granted',
            'ad_personalization': 'granted',
            'analytics_storage': 'granted'
        });
    }

    if(btnAccept) {
        btnAccept.addEventListener('click', function() {
            gtag('consent', 'update', {
                'ad_storage': 'granted',
                'ad_user_data': 'granted',
                'ad_personalization': 'granted',
                'analytics_storage': 'granted'
            });
            localStorage.setItem('consentStatus', 'granted');
            consentBanner.style.display = 'none';
        });
    }

    if(btnReject) {
        btnReject.addEventListener('click', function() {
            // Already denied by default in head
            localStorage.setItem('consentStatus', 'denied');
            consentBanner.style.display = 'none';
        });
    }
});
