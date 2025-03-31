import { createApp } from 'vue'
import './style.css'
import App from './App.vue'
import router from './router'

// Import FontAwesome Core
import { library } from "@fortawesome/fontawesome-svg-core";

// Import Specific Icons
import { 
  faUser, 
  faPhone, 
  faHome, 
  faMobileRetro,
  faPlus,
  faRotate,
} from "@fortawesome/free-solid-svg-icons";
import { faTelegram } from "@fortawesome/free-brands-svg-icons";

// Import FontAwesome Component
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";

// Add Icons to the Library
library.add(
  faUser, 
  faPhone, 
  faTelegram, 
  faHome, 
  faMobileRetro,
  faPlus,
  faRotate,
);

import Button from "./components/Button.vue";

createApp(App)
  .use(router)
  .component("font-awesome-icon", FontAwesomeIcon)
  .component("ui-button", Button)
  .mount('#app')
