from selenium import webdriver
import selenium.common
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.common.keys import Keys

def set_mobile_agent(profile):
    profile.set_preference("general.useragent.override", "Mozilla/5.0 (iPhone; CPU iPhone OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A334 Safari/7534.48.3")

def configure_proxy(caps, proxy_string):
    """
    proxy_string argument should have the format `host:port`
    """

    proxy = Proxy({
        'proxyType': ProxyType.MANUAL,
        'httpProxy': proxy_string,
        'ftpProxy': proxy_string,
        'sslProxy': proxy_string,
        'noProxy': '',
    })
    proxy.add_to_capabilities(caps)

if __name__ == "__main__":
    from argparse import ArgumentParser
    parser = ArgumentParser("Minimal Python Selenium example")
    parser.add_argument('--proxy', help='Format `host:port`', default=None)
    parser.add_argument('--user', help='Proxy user')
    parser.add_argument('--password', help='Proxy password')
    parser.add_argument('--headless', action='store_true', help='Run on headless environments (remote servers)')
    parser.add_argument('--mobile', action='store_true', help='Set user agent to mobile')

    args = parser.parse_args()

    profile = webdriver.FirefoxProfile()
    if args.mobile:
        set_mobile_agent(profile)

    caps = webdriver.DesiredCapabilities.FIREFOX.copy()

    if args.proxy:
        configure_proxy(caps, args.proxy)

    options = webdriver.firefox.options.Options()

    options.headless = args.headless

    print("Start a new Firefox driver")
    driver = webdriver.Firefox(profile, desired_capabilities=caps, options=options)

    bet365_url = "http://www.bet365.com/"
    print("Get %s" % bet365_url)
    driver.get(bet365_url)

    if args.user and args.password:
        print("Do proxy authentication")
        alert = WebDriverWait(driver, 10).until(EC.alert_is_present());
        alert.send_keys(args.user + Keys.TAB + args.password)
        alert.accept()
        # TODO check this succeeds

    print("Ready for action")
