export function deliveryAttemptRate(sent: number, attempted: number): number {
  return attempted === 0 ? 1 : sent / attempted;
}

export function targetDeliveryRate(): number {
  return 0.95;
}
