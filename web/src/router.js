import { createRouter, createWebHistory } from 'vue-router';

// Import your components
import Home from './pages/Home.vue';
import Accounts from './pages/Accounts.vue';
import AddAccount from './pages/AddAccount.vue';

// Define routes
const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home,
  },
  {
    path: '/accounts',
    name: 'Accounts',
    component: Accounts,
  },
  {
    path: "/accounts/add",
    name: "Add Account",
    component: AddAccount
  },
];

// Create the router instance
const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
