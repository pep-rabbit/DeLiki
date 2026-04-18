import polars as pl


def main():
    (
        pl.scan_csv(
            "./api/data/reimbursement_legal_entity_divisions_info.csv"
        ).with_columns(
            pl.col("medical_programs_in_divisions")
            .str.extract_all(r'"[^"]+"|[^,{}]+')
            .list.eval(pl.element().str.strip_chars().str.strip_chars('"'))
        )
    ).join(
        (
            pl.scan_csv("./api/data/payments_on_contracts_pharmacy_2025.csv")
            .group_by("legal_entity_edrpou")
            .agg(pl.col("pay_all").sum().alias("activity_score"))
            .select(
                "legal_entity_edrpou",
                "activity_score",
            )
        ),
        on="legal_entity_edrpou",
        how="inner",
    ).select(
        "legal_entity_name",
        "division_name",
        "division_addresses",
        "division_phone",
        "division_type",
        "division_settlement",
        "medical_programs_in_divisions",
        "activity_score",
    ).collect().write_parquet(
        "./api/data.parquet"
    )


if __name__ == "__main__":
    main()
