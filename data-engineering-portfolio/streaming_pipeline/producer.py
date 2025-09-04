# streaming_pipeline/producer.py
# Simple IoT-like event generator sending JSON messages to Kafka topic 'iot-events'.
# Usage:
#   python producer.py --bootstrap localhost:9092 --topic iot-events

import argparse, json, random, time
from datetime import datetime
from kafka import KafkaProducer

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--bootstrap", default="localhost:9092")
    parser.add_argument("--topic", default="iot-events")
    parser.add_argument("--rate", type=float, default=5.0, help="messages per second")
    args = parser.parse_args()

    producer = KafkaProducer(
        bootstrap_servers=args.bootstrap,
        value_serializer=lambda v: json.dumps(v).encode("utf-8"),
    )

    print(f"[producer] sending to {args.topic} at ~{args.rate} msg/s")
    delay = 1.0 / args.rate if args.rate > 0 else 0.0

    i = 0
    try:
        while True:
            event = {
                "device_id": random.randint(1, 20),
                "temp_c": round(random.uniform(20, 45), 2),
                "humidity": round(random.uniform(30, 80), 2),
                "ts": datetime.utcnow().isoformat() + "Z",
            }
            producer.send(args.topic, event)
            i += 1
            if i % 50 == 0:
                print(f"[producer] sent {i} messages")
            time.sleep(delay)
    except KeyboardInterrupt:
        print("\n[producer] stopping...")

if __name__ == "__main__":
    main()