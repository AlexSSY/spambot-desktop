import { createRouter, createWebHistory } from 'vue-router';

// Import your components
import Home from './pages/Home.vue';
import About from './pages/About.vue';

// Define routes
const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home,
  },
  {
    path: '/about',
    name: 'About',
    component: About,
  },
];

// Create the router instance
const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
