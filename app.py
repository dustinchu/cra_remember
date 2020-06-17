from pyquery import PyQuery


html = '''
  <div class="flymenu" id="header__storage">
   <div class="header__bottom">
    <div class="flymenu__tray">
     <a class="header__logo" href="/zh">
      <img alt="Digi-Key Electronics - Electronic Components Distributor" src="//www.digikey.tw/-/media/Images/Header/logo_dk.png?la=zh-TW&amp;ts=1a773fa3-b656-418a-8e50-67fff895081a"/>
     </a>
     <span class="flymenu__trigger icon-close">
     </span>
    </div>
    <div class="flymenu__nav-bar">
     <div class="flymenu__container">
      <ul class="flymenu__sections" cookie-event="ref_page_event=Header Nav">
       <li class="flymenu__section">
        <a class="flymenu__section-title" data-level="1" href="/products/zh">
         產品
        </a>
        <div class="flymenu__section-contents">
         <div class="flymenu__column">
          <a class="flymenu__back">
           返回
          </a>
          <ul class="flymenu__items">
           <li class="flymenu__item">
            <a class="flymenu__item-title" data-level="2" href="/products/leds-optoelectronics/zh/">
             LED／光電子產品
            </a>
            <div class="flymenu__column">
             <a class="flymenu__back">
              返回
             </a>
             <ul class="">
              <li class="flymenu__item">
               <a class="flymenu__item-title" href="/products/zh/optoelectronics/led-indication-discrete/105">
                LED 指示燈 - 離散
               </a>
              </li>
              <li class="flymenu__item">
               <a class="flymenu__item-title" href="/products/zh/optoelectronics/led-lighting-cobs-engines-modules-strips/111">
                LED 照明 - COB、引擎、模組、燈條
               </a>
              </li>
              <li class="flymenu__item">
               <a class="flymenu__item-title" href="/products/zh/optoelectronics/led-lighting-white/124">
                LED 照明 - 白光
               </a>
              </li>
              <li class="flymenu__item">
               <a class="flymenu__item-title" href="/products/zh/optoelectronics/led-lighting-color/125">
                LED 照明 - 彩色
               </a>
              </li>
              <li class="flymenu__item">
               <a class="flymenu__item-title" href="/products/zh/optoelectronics/panel-indicators-pilot-lights/108">
                面板指示器、指示燈
               </a>
              </li>
              <li class="flymenu__item">
               <a class="flymenu__item-title" href="/products/zh/optoelectronics/laser-diodes-modules/95">
                雷射二極體、模組
               </a>
              </li>
              <li class="flymenu__item">
               <a class="flymenu__item-title" href="/products/zh/optoelectronics/fiber-optics-transceiver-modules/118">
                光纖 - 收發器模組
               </a>
              </li>
              <li class="flymenu__item">
               <a class="flymenu__item-title" href="/products/zh/optoelectronics/optics-light-pipes/102">
                光學 - 光導管
               </a>
              </li>
              <li class="flymenu__item">
               <a class="flymenu__item-title" href="/products/zh/optoelectronics/infrared-uv-visible-emitters/94">
                紅外線、UV、可見光發射器
               </a>
              </li>
              <li class="flymenu__item">
               <a class="flymenu__item-title" href="/products/zh/optoelectronics/display-modules-lcd-oled-character-and-numeric/99">
                顯示器模組 - LCD、OLED 字元和數字
               </a>
              </li>
              <li class="flymenu__item">
               <a class="flymenu__item-title" href="/products/zh/optoelectronics/display-modules-lcd-oled-graphic/107">
                顯示器模組 - LCD、OLED、圖像
               </a>
              </li>
              <li class="flymenu__item">
               <a class="flymenu__item-title" href="/products/zh/optoelectronics/display-modules-led-character-and-numeric/92">
                顯示器模組 - LED 字元和數字
               </a>
              </li>
              <li class="flymenu__item flymenu__more">
               <a class="flymenu__item-title" href="/products/leds-optoelectronics/zh">
                查看全部
               </a>
              </li>
             </ul>
             <a href="/products/zh/optoelectronics/led-lighting-cobs-engines-modules-strips/111?v=1697,90,2138">
              <div class="flymenu__featured" data-img="//www.digikey.tw/-/media/Images/ENavHeader/main-cat-flyouts/2020/Newhaven_Product-Flyouts.jpg?la=zh-TW&amp;ts=4f7b91a5-986c-4441-813e-c6d06e96f174">
               <div class="flymenu__featured__logo" data-img="//www.digikey.tw/-/media/Images/Logos/cree_wolfspeed_color.png?la=zh-TW&amp;ts=9e285f0b-8774-478a-b084-60a3a8d2de09&amp;w=200&amp;h=100">
               </div>
               <span class="flymenu__featured-text">
                LED 照明 - COB、引擎、模組、燈條
               </span>
              </div>
             </a>
            </div>
           </li>
           <li class="flymenu__item">
            <a class="flymenu__item-title" data-level="2" href="/products/zh/rf-if-and-rfid/37">
             RF/IF 和 RFID
            </a>
            <div class="flymenu__column">
             <a class="flymenu__back">
              返回
             </a>
             <ul class="">
              <li class="flymenu__item">
               <a class="flymenu__item-title" href="/products/zh/rf-if-and-rfid/rf-shields/867">
                RF 屏蔽
               </a>
              </li>
              <li class="flymenu__item">
               <a class="flymenu__item-title" href="/products/zh/rf-if-and-rfid/rf-evaluation-and-development-kits-boards/859">
                RF 評估和開發套件、板件
               </a>
              </li>
              <li class="flymenu__item">
               <a class="flymenu__item-title" href="/products/zh/rf-if-and-rfid/rf-amplifiers/860">
                RF 放大器
               </a>
              </li>
              <li class="flymenu__item">
               <a class="flymenu__item-title" href="/products/zh/rf-if-and-rfid/rf-directional-coupler/850">
                RF 定向耦合器
               </a>
              </li>
              <li class="flymenu__item">
               <a class="flymenu__item-title" href="/products/zh/rf-if-and-rfid/rf-antennas/875">
                RF 天線
               </a>
              </li>
              <li class="flymenu__item">
               <a class="flymenu__item-title" href="/products/zh/rf-if-and-rfid/rf-switches/865">
                RF 開關
               </a>
              </li>
              <li class="flymenu__item">
               <a class="flymenu__item-title" href="/products/zh/rf-if-and-rfid/rf-mixers/861">
                RF 混頻器
               </a>
              </li>
              <li class="flymenu__item">
               <a class="flymenu__item-title" href="/products/zh/rf-if-and-rfid/rf-receiver-transmitter-and-transceiver-finished-units/873">
                RF 接收器、發射器和收發器成品
               </a>
              </li>
              <li class="flymenu__item">
               <a class="flymenu__item-title" href="/products/zh/rf-if-and-rfid/rf-detectors/862">
                RF 偵測器
               </a>
              </li>
              <li class="flymenu__item">
               <a class="flymenu__item-title" href="/products/zh/rf-if-and-rfid/rf-transceiver-ics/879">
                RF 收發器 IC
               </a>
              </li>
              <li class="flymenu__item">
               <a class="flymenu__item-title" href="/products/zh/rf-if-and-rfid/rf-transceiver-modules/872">
                RF 收發器模組
               </a>
              </li>
              <li class="flymenu__item">
               <a class="flymenu__item-title" href="/products/zh/rf-if-and-rfid/balun/849">
                平衡不平衡轉換器
               </a>
              </li>
              <li class="flymenu__item flymenu__more">
               <a class="flymenu__item-title" href="/products/zh/rf-if-and-rfid/37">
                查看全部
               </a>
              </li>
             </ul>
             <a href="/products/zh/rf-if-and-rfid/rf-antennas/875?v=478,939">
              <div class="flymenu__featured" data-img="//www.digikey.tw/-/media/Images/ENavHeader/main-cat-flyouts/2020/AVX_flyout.jpg?la=zh-TW&amp;ts=3f1e8416-5a22-4f30-ab42-0d79c8ef3573">
               <div class="flymenu__featured__logo" data-img="//www.digikey.tw/-/media/Images/Logos/avx_color.png?la=zh-TW&amp;ts=87232539-0b8f-4eed-87ed-fc6415793358&amp;w=200&amp;h=100">
               </div>
               <span class="flymenu__featured-text">
                RF 天線
               </span>
              </div>
             </a>
            </div>
           </li>
           <li class="flymenu__item">
            <a class="flymenu__item-title" data-level="2" href="/products/passives/zh/">
             被動
            </a>
            <div class="flymenu__column">
             <a class="flymenu__back">
              返回
             </a>
             <ul class="">
              <li class="flymenu__item">
               <a class="flymenu__item-title" data-level="3" href="/products/zh/crystals-oscillators-resonators/oscillators/172">
                振盪器
               </a>
               <div class="flymenu__column">
                <a class="flymenu__back">
                 返回
                </a>
                <ul class="">
                 <li class="flymenu__item">
                  <a class="flymenu__item-title" href="/products/zh/crystals-oscillators-resonators/pin-configurable-selectable-oscillators/176">
                   引腳可配置／可選擇振盪器
                  </a>
                 </li>
                 <li class="flymenu__item">
                  <a class="flymenu__item-title" href="/products/zh/crystals-oscillators-resonators/programmable-oscillators/169">
                   可編程振盪器
                  </a>
                 </li>
                 <li class="flymenu__item">
                  <a class="flymenu__item-title" href="/products/zh/crystals-oscillators-resonators/oscillators/172">
                   振盪器
                  </a>
                 </li>
                 <li class="flymenu__item">
                  <a class="flymenu__item-title" href="/products/zh/crystals-oscillators-resonators/sockets-and-insulators/175">
                   插槽和絕緣體
                  </a>
                 </li>
                 <li class="flymenu__item">
                  <a class="flymenu__item-title" href="/products/zh/crystals-oscillators-resonators/stand-alone-programmers/170">
                   獨立編程器
                  </a>
                 </li>
                 <li class="flymenu__item">
                  <a class="flymenu__item-title" href="/products/zh/crystals-oscillators-resonators/vcos-voltage-controlled-oscillators/173">
                   壓控振盪器 (VCO)
                  </a>
                 </li>
                </ul>
               </div>
              </li>
'''
# doc = PyQuery(html)
doc = PyQuery(url='https://www.digikey.tw/products/zh')
# li = doc('a.flymenu__item-title')
for home in doc.items('.catfilters'):
    for home_body in home('.indexNewIndicator > a'):
        print(home_body)
        for title in doc.items('a.flymenu__item-title'):
            print("https://www.digikey.tw"+PyQuery(title).attr['href'])
            print(title.text())

