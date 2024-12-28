import logging
import warnings
from urllib3.exceptions import NotOpenSSLWarning

logging.captureWarnings(True)
warnings.filterwarnings("ignore", category=NotOpenSSLWarning)

from modules.crawler import crawl
from modules.vulnerability_scanner import test_sql_injection, test_xss
from modules.report_generator import generate_report

def main():
    base_url = input("Enter the URL to scan: ").strip()
    print(f"Crawling: {base_url}")
    
    urls = crawl(base_url)
    print(f"Found {len(urls)} URLs to scan.")

    vulnerabilities = []
    for url in urls:
        print(f"Scanning {url} for vulnerabilities...")
        
        # Test SQL Injection
        test_sql_injection(url)
        vulnerabilities.append({"url": url, "type": "SQL Injection"})
        
        # Test XSS
        test_xss(url)
        vulnerabilities.append({"url": url, "type": "XSS"})
    
    generate_report(vulnerabilities)

if __name__ == "__main__":
    main()
