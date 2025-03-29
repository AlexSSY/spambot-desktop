<script setup>
</script>

<template>
  <h1 class="text-red-300">Hello World!</h1>
  <nav>
      <ul>
        <li><router-link to="/">Home</router-link></li>
        <li><router-link to="/about">About</router-link></li>
      </ul>
    </nav>
  <router-view></router-view>
</template>
