<script setup></script>

<template>
  <form class="flex flex-col space-y-2" @submit.prevent="submitForm">
    <input v-model="phone" type="text" class="text-black" />
    <span v-if="phoneError">{{ phoneError }}</span>
    <button type="submit">Add</button>
    <span v-if="responseMessage">{{ responseMessage }}</span>
  </form>
</template>

<script>
export default {
  data() {
    return {
      phone: "",
      phoneError: "",
      responseMessage: ""
    };
  },
  methods: {
    validatePhone() {
      const phoneRegex = /^\+?[1-9]\d{1,14}$/;

      if (!this.phone.match(phoneRegex)) {
        this.phoneError = "Invalid phone number format";
        return false;
      }

      this.phoneError = "";

      return true;
    },
    async submitForm() {
      try {
        if (!this.validatePhone()) {
          return;
        }

        const response = await fetch("/api/accounts/add/", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ phone: this.phone }),
        });

        const result = await response.json();
        this.responseMessage = result;
      } catch (error) {
        console.error("Error submitting form:", error);
      }
    },
  },
};
</script>
