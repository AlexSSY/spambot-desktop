<template>
  <ul class="flex items-center space-x-3">
    <li>
      <router-link to="/" class="flex items-center space-x-2">
        <font-awesome-icon
          :icon="['fa', 'home']"
          class="text-blue-400 hover:text-blue-200 text-base"
        />
        <span>Home</span>
      </router-link>
    </li>
    <li>
      <router-link to="/accounts" class="flex items-center space-x-2">
        <font-awesome-icon
          :icon="['fa', 'mobile-retro']"
          class="text-blue-400 hover:text-blue-200 text-base"
        />
        <span>Accounts</span>
      </router-link>
    </li>
    <li>
      <router-link to="/accounts/add" class="flex items-center space-x-2">
        <font-awesome-icon
          :icon="['fa', 'plus']"
          class="text-blue-400 hover:text-blue-200 text-base"
        />
        <span>Add Account</span>
      </router-link>
    </li>
  </ul>
</template>
